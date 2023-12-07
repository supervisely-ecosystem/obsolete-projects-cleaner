<div align='center' markdown> 
<img src="https://github.com/supervisely-ecosystem/obsolete-dataset-cleaner/assets/57998637/34142660-e406-4474-b86c-3ef541c1b7f5"/> <br>

# Obsolete Datasets Cleaner

<p align='center'>
  <a href='#overview'>Overview</a> •
  <a href='#application-settings'>How to Run</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/obsolete-dataset-cleaner)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/obsolete-dataset-cleaner)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/obsolete-dataset-cleaner.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/obsolete-dataset-cleaner.png)](https://supervise.ly)

</div>

## Overview

This application allows administrators to purge projects of obsolete datasets without saving them to the `Trash Bin`.
  
## Application Settings

### Select Workspace

Here you can choose one of:
 - a specific workspace for whose projects all datasets will be deleted
 - all available workspaces for whose projects all datasets will be deleted

### Dataset Age

Set the number of days to determine how long ago the datasets were created, starting now.

### Sleep Time

Set the number of days the application will wait for the next cleaning iteration after the current one is complete.

### Additional Settings

Check the `One-time task` checkbox to run the application only once.