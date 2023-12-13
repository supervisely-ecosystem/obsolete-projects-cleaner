import os

import supervisely as sly
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

task_id = sly.env.task_id()
workspace_id = sly.env.workspace_id()
if workspace_id is not None:
    workspace_id = int(workspace_id)

age = 1

sleep_days = 1
sleep_time = sleep_days * 86400

all_workspaces = True

all_projects = True
project_id = None

delete_projects = True
delete_datasets = False

updated = True
created = False

delete_permanently = False

one_time_task = False

items_to_delete = None
item_type = "project"
