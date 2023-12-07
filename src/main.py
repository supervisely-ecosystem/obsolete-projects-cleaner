import time
from datetime import datetime, timedelta
from typing import Optional

import globals as g
import supervisely as sly


def get_dataset_infos(workspace_id: Optional[int]):
    kwargs = {}
    filters = []

    kwargs["page"] = "all"  # to get all available datasets in a single 2nd request

    if g.age != 0:
        current_datetime = datetime.utcnow()
        dataset_age = current_datetime - timedelta(days=g.age)
        formatted_timestamp = dataset_age.strftime("%Y-%m-%dT%H:%M:%SZ")
        time_filter = {
            "field": "createdAt",
            "operator": "<",
            "value": formatted_timestamp,
        }
        filters.append(time_filter)

    if workspace_id is not None:
        ws_filter = {
            "field": "workspaceId",
            "operator": "=",
            "value": workspace_id,
        }
        filters.append(ws_filter)

    if len(filters) != 0:
        kwargs["filters"] = filters

    response_json = g.api.dataset.get_list_all(**kwargs)

    return response_json.get("entities")


def choose_workspace():
    if not g.all_workspaces:
        return g.workspace_id
    else:
        return None


def process_datasets():
    while True:
        workspace_id = choose_workspace()
        dataset_infos = get_dataset_infos(workspace_id)

        num_of_datasets = len(dataset_infos)

        if num_of_datasets != 0:
            ids = [dataset_info.get("id") for dataset_info in dataset_infos]
            g.api.dataset.remove_permanently(ids)

        if g.stop:
            g.api.logger.info(f"🔚 Task accomplished. {num_of_datasets} dataset(s) deleted")
            break
        else:
            next_run = (datetime.utcnow() + timedelta(seconds=g.sleep_time)).strftime(
                "%Y-%m-%d %H:%M:%S UTC+0"
            )
            g.api.logger.info(
                f"""🔚 Task accomplished. 
                {num_of_datasets} dataset(s) deleted.
                'Sleep' mode activated.
                The next iteration will start on {next_run}
            """
            )
            g.api.logger.info(f"")
            time.sleep(g.sleep_time)


def main():
    process_datasets()


if __name__ == "__main__":
    sly.main_wrapper("main", main)
