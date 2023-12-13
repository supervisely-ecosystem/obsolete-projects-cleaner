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

This application allows deleting unused `Projects` or their `Datasets` in large batches.
  
## How to Run

### All available Workspaces

 - **Checked**: `Projects` or its `Datasets` will be deleted in all available `Workspaces`.
 - **Unchecked**: `Projects` or its `Datasets` will be deleted in selected `Workspace`.

### All available Projects

ℹ️ Only for entity type `Datasets`.

 - **Checked**: `Datasets` will be deleted in all available `Projects` of selected `Workspace`.
 - **Unchecked**: `Datasets` will be deleted in selected `Project` of selected `Workspace`

### Entity type
  - **`Projects`**
  - **`Datasets`**

### Filter criteria

 - **Updated**
 - **Created**

Set the number of days to determine how long ago the datasets were created or updated last time.
  
### Method
 - **Delete to Trash Bin**
 - **Delete permanently**


### Launch type
 - **Repetitive Task**
    - **Sleep day(s)**: Set the number of days the application will wait for the next cleaning iteration after the current one is complete.
 - **One-time Task**: run the application only once.


