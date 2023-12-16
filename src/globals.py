import os

import supervisely as sly
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()


all_workspaces = True
all_projects = True
workspace_id = None
project_id = None

delete_projects = True
delete_datasets = False
item_type = "project"

updated = True
created = False

age = 1
sleep_days = 1

delete_permanently = False
one_time_task = False

items_to_delete = None
