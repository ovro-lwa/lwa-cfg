# lwa-cfg

Currently the Excel spreadsheet in this repo is driving the system configuration used by subsystems in LWA. Other configuration files can be added. YAML format is preferred.

## WORKFLOW

Changes to the Excel spreadsheet must be done to the file in Sharepoint. When a consistent set of changes is complete, copy the file into a working tree of this repo. Ensure the working tree is up to date with the remote reposisotry. Commit the file with a commit message of less than 80 characters. If more detail is needed, do so after a blank line in the message. Push the change to the repo and click the ***Upload System config*** button in the Web UI or send an upload command to the service via etcd. The etcd key being: /cmd/cfg.

The contents of the Excel spreadsheet will be converted to YAML and committed as the lwacfgsrv user. This file can be easily diff'd with git. It will also be pushed into Etcd under the ***/cfg/system*** key. Subsystems can register callbacks on this key to dynamically update on changes.
