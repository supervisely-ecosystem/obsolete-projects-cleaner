import time
from datetime import datetime, timedelta
from typing import Union, List

import supervisely as sly

import src.globals as g
import src.ui as ui

app = sly.Application(layout=ui.layout)


def apply_filters(kwargs: dict, filters: list):
    if g.age != 0:
        current_datetime = datetime.utcnow()
        dataset_age = current_datetime - timedelta(days=g.age)
        formatted_timestamp = dataset_age.strftime("%Y-%m-%dT%H:%M:%SZ")
        if g.created and not g.updated:
            time_filter = {
                "field": "createdAt",
                "operator": "<=",
                "value": formatted_timestamp,
            }
        elif g.updated and not g.created:
            time_filter = {
                "field": "updatedAt",
                "operator": "<=",
                "value": formatted_timestamp,
            }
        filters.append(time_filter)

    if g.workspace_id is not None:
        ws_filter = {
            "field": "workspaceId",
            "operator": "=",
            "value": g.workspace_id,
        }
        filters.append(ws_filter)

    return kwargs if len(filters) == 0 else {**kwargs, "filters": filters}


def get_dataset_infos() -> list:
    kwargs = {"page": "all"}  # to get all available datasets in a single 2nd request
    filters = []

    if g.project_id is not None and not g.all_projects:
        pr_filter = {
            "field": "projectId",
            "operator": "=",
            "value": g.project_id,
        }
        filters.append(pr_filter)

    kwargs = apply_filters(kwargs, filters)
    response_json = g.api.dataset.get_list_all(**kwargs)

    return response_json.get("entities")


def get_project_infos() -> list:
    kwargs = {"page": "all"}  # to get all available projects in a single 2nd request
    filters = []

    kwargs = apply_filters(kwargs, filters)
    response_json = g.api.project.get_list_all(**kwargs)

    return response_json.get("entities")


def adjust_workspace_id():
    if g.all_workspaces:
        g.workspace_id = None


def get_items():
    adjust_workspace_id()
    if g.delete_projects and not g.delete_datasets:
        g.items_to_delete = get_project_infos()
    elif g.delete_datasets and not g.delete_projects:
        g.items_to_delete = get_dataset_infos()


def prepare_batches(item_infos: List[Union[sly.ProjectInfo, sly.DatasetInfo]]):
    batches = []
    for item_info in item_infos:
        if any(d["team_id"] == item_info.team_id for d in batches):
            for d in batches:
                if d["team_id"] == item_info.team_id:
                    d["ids"].append(item_info.id)
                    break
        else:
            batch = {"team_id": item_info.team_id, "ids": [item_info.id]}
            batches.append(batch)
    return batches


def delete_entities():
    with app.handle_stop():
        iteration = 0
        while True:
            iteration += 1
            if not g.one_time_task and iteration > 1:
                get_items()
                ui.selected_entities_field.set(
                    text=f"{len(g.items_to_delete)} {g.item_type}(s) will be deleted", status="text"
                )
            ui.next_run_card.hide()
            ui.delete_btn.button_type = "success"
            ui.delete_btn.text = "Processing"
            ui.delete_btn.icon = "zmdi zmdi-wrench"
            if len(g.items_to_delete) != 0:
                batches = prepare_batches(g.items_to_delete)
                for batch in batches:
                    ids = batch["ids"]
                    if g.item_type == "dataset":
                        if g.delete_permanently:
                            g.api.dataset.remove_permanently(ids)
                        else:
                            g.api.dataset.remove_batch(ids)
                    elif g.item_type == "project":
                        if g.delete_permanently:
                            g.api.project.remove_permanently(ids)
                        else:
                            g.api.project.remove_batch(ids)

            if g.one_time_task:
                g.api.logger.info(
                    f"🔚 Task accomplished. {len(g.items_to_delete)} {g.item_type}(s) deleted"
                )
                ui.selected_entities_field.set(
                    text=f"{len(g.items_to_delete)} {g.item_type}(s) deleted", status="success"
                )
                ui.delete_btn.button_type = "success"
                ui.delete_btn.icon = "zmdi zmdi-check"
                ui.delete_btn.text = "Finished"
                break
            else:
                next_run = (datetime.utcnow() + timedelta(days=g.sleep_days)).strftime(
                    "%Y-%m-%d %H:%M:%S UTC+0"
                )
                g.api.logger.info(
                    f"""🔚 Task accomplished. 
                    {len(g.items_to_delete)} dataset(s) deleted.
                    'Sleep' mode activated.
                    The next iteration will start on {next_run}
                """
                )
                ui.delete_btn.button_type = "warning"
                ui.delete_btn.text = "Sleep"
                ui.delete_btn.icon = "zmdi zmdi-alarm"
                ui.nex_run_field.set(f"Date and time: {next_run}", "text")
                ui.next_run_card.show()
                ui.selected_entities_field.set(
                    text=f"{len(g.items_to_delete)} {g.item_type}(s) deleted", status="success"
                )
                time.sleep(g.sleep_days * 86400)
        app.stop()
