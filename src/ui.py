from typing import Literal

import supervisely as sly
from supervisely.app.widgets import (
    Button,
    Card,
    Checkbox,
    Container,
    Field,
    InputNumber,
    NotificationBox,
    RadioGroup,
    SelectProject,
    SelectWorkspace,
    Text,
)

import src.globals as g
import src.main as m

#### Radio Groups ####

entities_items = [
    RadioGroup.Item(value="projects", label="Projects"),
    RadioGroup.Item(value="datasets", label="Datasets"),
]
entities_radio_group = RadioGroup(items=entities_items, size="large")
entities_container = Container([entities_radio_group], style="margin-left: 20px;")
entities_field = Field(title="Entity type", content=entities_container)


entity_age_input = InputNumber(g.age, 1, 720)
entity_age_text = Text(text="Day(s) ago")
entity_age_container = Container([entity_age_text, entity_age_input])
filter_criteria_items = [
    RadioGroup.Item(value="updated_at", label="Updated"),
    RadioGroup.Item(value="created_at", label="Created"),
]
filter_criteria_radio_group = RadioGroup(items=filter_criteria_items, size="large")
filter_criteria_container = Container(
    [filter_criteria_radio_group, entity_age_container], style="margin-left: 20px;"
)
filter_criteria_field = Field(title="Filter criteria", content=filter_criteria_container)


removal_method_items = [
    RadioGroup.Item(value="trash_bin", label="Delete to Trash Bin"),
    RadioGroup.Item(value="permanently", label="Delete permanently"),
]
removal_method_radio_group = RadioGroup(items=removal_method_items, size="large")
removal_method_notification_box = NotificationBox(
    title="!!! WARNING !!!",
    description="Be careful, this method deletes data from the database, recovery is not possible.",
    box_type="warning",
)
removal_method_notification_box.hide()
removal_method_container = Container(
    [removal_method_radio_group, removal_method_notification_box],
    style="margin-left: 20px;",
)
removal_method_field = Field(title="Method", content=removal_method_container)


#### Settings ####

save_settings_btn = Button("Save settings", icon="zmdi zmdi-save")

workspace_dropdown = SelectWorkspace()
workspace_dropdown_field = Field(title="Select Workspace", content=workspace_dropdown)
workspace_dropdown_field.hide()

project_dropdown = SelectProject()
project_dropdown_field = Field(title="Select Project", content=project_dropdown)
project_dropdown_field.hide()

dropdows_container = Container(
    [workspace_dropdown_field, project_dropdown_field], gap=0, style="margin-left: 20px;"
)
dropdows_container.hide()

all_workspaces_checkbox = Checkbox(content="All available Workspaces", checked=True)
all_workspaces_checkbox.check()

all_projects_checkbox = Checkbox(content="All available Projects", checked=True)
all_projects_checkbox.check()
all_projects_checkbox.hide()

sleep_days_input = InputNumber(g.sleep_days, 1, 180)
sleep_days_text = Text(text="Sleep day(s)")
sleep_days_container = Container([sleep_days_text, sleep_days_input], style="margin-left: 27px;")
launch_type_items = [
    RadioGroup.Item(value="cycle", label="Repetitive Task"),
    RadioGroup.Item(value="one", label="One-time Task"),
]
launch_type_radio_group = RadioGroup(items=launch_type_items, size="large")
launch_type_container = Container(
    [launch_type_radio_group, sleep_days_container], style="margin-left: 20px;"
)
launch_type_field = Field(title="Launch type", content=launch_type_container)

team_checkboxes_container = Container(
    [all_workspaces_checkbox, all_projects_checkbox],
    direction="horizontal",
)

workspaces_container = Container([team_checkboxes_container, dropdows_container])

settings_container = Container(
    [
        workspaces_container,
        entities_field,
        filter_criteria_field,
        removal_method_field,
        launch_type_field,
    ]
)
settings_card = Card(title="Settings", content=settings_container)


#### Entities ####

delete_btn = Button("Delete", icon="zmdi zmdi-play", button_type="danger")
delete_btn.disable()

save_settings_btn = Button("Save settings", icon="zmdi zmdi-save")
selected_entities_field = Text(
    text="After the settings have been saved, the number of entities to be deleted will be displayed here and 'Delete' button will be unlocked",
    status="info",
)
entities_card_container = Container([selected_entities_field, delete_btn], gap=20)
entities_card = Card("Number of entities to be deleted", content=entities_card_container)

nex_run_field = Text()
next_run_card = Card("Next run", content=nex_run_field)
next_run_card.hide()

#### Main Containers ####

left_container = Container(
    widgets=[
        settings_card,
        save_settings_btn,
    ],
    style="flex: 1 1 0%;/* display: flex; */",
)

righ_container = Container(
    widgets=[
        entities_card,
        next_run_card,
    ],
    style="flex: 2 1 0%;/* display: flex; */",
)

layout = Container(
    [left_container, righ_container],
    direction="horizontal",
    fractions=[1, 2],
)


def change_setting_status(status: Literal["enable", "disable"]):
    if status == "enable":
        all_projects_checkbox.enable()
        all_workspaces_checkbox.enable()
        workspace_dropdown.enable()
        project_dropdown.enable()
        entities_radio_group.enable()
        entity_age_input.enable()
        filter_criteria_radio_group.enable()
        removal_method_radio_group.enable()
        launch_type_radio_group.enable()
        sleep_days_input.enable()
    elif status == "disable":
        all_projects_checkbox.disable()
        all_workspaces_checkbox.disable()
        workspace_dropdown.disable()
        project_dropdown.disable()
        entities_radio_group.disable()
        entity_age_input.disable()
        filter_criteria_radio_group.disable()
        removal_method_radio_group.disable()
        launch_type_radio_group.disable()
        sleep_days_input.disable()


def show_globals():
    sly.logger.debug(
        f"""
            Settings:
                all_workspaces = {g.all_workspaces} | all_projects = {g.all_projects}
                workspace_id = {g.workspace_id}   | project_id = {g.project_id}
                
                delete_projects = {g.delete_projects} | delete_datasets = {g.delete_datasets}
                item_type = {g.item_type}

                updated = {g.updated} | created = {g.created}
                age = {g.age}

                delete_permanently = {g.delete_permanently}

                one_time_task = {g.one_time_task} | sleep_days = {g.sleep_days} 
        """
    )


### Event Handlers ###


@delete_btn.click
def delete_entities():
    save_settings_btn.disable()
    m.delete_entities()


@save_settings_btn.click
def get_items_for_deletion():
    if save_settings_btn.button_type == "primary":
        if not all_workspaces_checkbox.is_checked():
            g.workspace_id = workspace_dropdown.get_selected_id()
        if not all_projects_checkbox.is_checked():
            g.project_id = project_dropdown.get_selected_id()
        if not g.all_projects and g.project_id is None:
            text = "No project has been selected. Please select a project from the drop-down list to continue processing."
            sly.app.show_dialog(title="Project Error", description=text, status="error")
            raise ValueError(text)

        show_globals()
        m.get_items()
        selected_entities_field.set(
            text=f"{len(g.items_to_delete)} {g.item_type}(s) will be deleted", status="text"
        )
        delete_btn.enable()
        change_setting_status(status="disable")
        save_settings_btn.button_type = "success"
        save_settings_btn.text = "Change settings"
        save_settings_btn.icon = "zmdi zmdi-rotate-left"
    elif save_settings_btn.button_type == "success":
        delete_btn.disable()
        change_setting_status(status="enable")
        save_settings_btn.button_type = "primary"
        save_settings_btn.text = "Save settings"
        save_settings_btn.icon = "zmdi zmdi-save"
        selected_entities_field.set(
            text="After the settings have been saved, the number of entities to be deleted will be displayed here and 'Delete' button will be unlocked",
            status="info",
        )


@all_workspaces_checkbox.value_changed
def set_all_workspaces_param(checked):
    if checked is True:
        dropdows_container.hide()
        g.workspace_id = None
        g.project_id = None
        g.all_workspaces = True
        g.all_projects = True
        all_projects_checkbox.hide()
        all_projects_checkbox.check()
    else:
        if g.delete_datasets is True:
            all_projects_checkbox.show()
            all_projects_checkbox.check()
        project_dropdown_field.hide()
        workspace_dropdown_field.show()
        dropdows_container.show()
        g.all_workspaces = False


@all_projects_checkbox.value_changed
def set_all_projects_param(checked):
    if checked is True:
        project_dropdown_field.hide()
        workspace_dropdown_field.show()
        dropdows_container.show()
        g.project_id = None
        g.all_projects = True
    else:
        project_dropdown_field.show()
        workspace_dropdown_field.hide()
        dropdows_container.show()
        g.all_projects = False


@entities_radio_group.value_changed
def set_entity_value(value):
    if value == "projects":
        g.item_type = "project"
        g.all_projects = True
        g.project_id = None
        g.delete_projects = True
        g.delete_datasets = False
        if g.all_workspaces is False:
            all_projects_checkbox.hide()
            all_projects_checkbox.check()
            project_dropdown_field.hide()
            workspace_dropdown_field.show()
            dropdows_container.show()
    else:
        g.item_type = "dataset"
        g.delete_datasets = True
        g.delete_projects = False
        if g.all_workspaces is False:
            all_projects_checkbox.show()
            all_projects_checkbox.check()


@filter_criteria_radio_group.value_changed
def set_filter_value(value):
    if value == "updated_at":
        g.updated = True
        g.created = False
    else:
        g.updated = False
        g.created = True


@removal_method_radio_group.value_changed
def set_delete_value(value):
    if value == "permanently":
        g.delete_permanently = True
        removal_method_notification_box.show()
    else:
        g.delete_permanently = False
        removal_method_notification_box.hide()


@launch_type_radio_group.value_changed
def change_launch_type(value):
    if value == "one":
        g.one_time_task = True
        sleep_days_container.hide()
    else:
        g.one_time_task = False
        sleep_days_container.show()


@sleep_days_input.value_changed
def change_sleep_days(value):
    g.sleep_days = int(value)


@entity_age_input.value_changed
def change_entity_age(value):
    g.age = int(value)
