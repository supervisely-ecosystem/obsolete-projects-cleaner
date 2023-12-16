<div align='center' markdown> 
<img src="https://github.com/supervisely-ecosystem/obsolete-projects-cleaner/assets/57998637/aae36fe0-33b2-41f9-9968-a1c4ab119674"/> <br>

# Obsolete Projects Cleaner

<p align='center'>
  <a href='#overview'>Overview</a> •
  <a href='#how-to-run'>How to Run</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/obsolete-projects-cleaner)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/obsolete-projects-cleaner)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/obsolete-projects-cleaner.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/obsolete-projects-cleaner.png)](https://supervise.ly)

</div>

## Overview

This application allows you to delete unused `Projects` or their `Datasets` in large batches by a given filtering criterion.
  
## How to Run

### All available Workspaces

 - **Checked**: `Projects` or its `Datasets` will be deleted in all available `Workspaces`.
 - **Unchecked**: `Projects` or its `Datasets` will be deleted in selected `Workspace`.

### All available Projects

ℹ️ Only for entity type `Datasets`.

 - **Checked**: `Datasets` will be deleted in all available `Projects` of selected `Workspace`.
 - **Unchecked**: `Datasets` will be deleted in selected `Project` of selected `Workspace`

### Entity type
  - **`Projects`** - You can think of a Project as a superfolder with data and metadata, like classes and tags. Every dataset inside the project will share the same metadata and have the same classes and tags defined on the project-level. [Read more.](https://docs.supervisely.com/data-organization/projects)
  - **`Datasets`** - Dataset is the second most important concept in Supervisely. Here is where your labeled and unlabeled images and images, videos, and so on. There is no more levels: images or videos are directly attached to a dataset. [Read more.](https://docs.supervisely.com/data-organization/projects/datasets)

### Filter criteria

 - **Updated** - specifies the timestamp of the last update, all entities updated before this timestamp will be deleted.
 - **Created** - specifies the creation timestamp, all entities created before this timestamp will be deleted.

    The time stamp is calculated in days, the maximum value that can be set is 720 days.
  
### Method
 - **Delete to Trash Bin** - this method will not delete your data immediately, it will be stored in the recycle bin for 7 days before being completely deleted.
 - **Delete permanently** - this method will immediately delete data. This means that all data will be deleted from the database with no possibility to restore it.


### Launch type
 - **Repetitive Task**
    - **Sleep day(s)** - the number of days the application will wait for the next cleaning iteration after the current one is complete. 
      
      The maximum value that can be set is 180 days.
 - **One-time Task** - run the application only once.


