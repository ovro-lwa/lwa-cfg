# lwa-cfg

Currently the Excel spreadsheet in this repo is driving the system configuration used by subsystems in LWA. Other configuration files can be added. YAML format is preferred.

## WORKFLOW

Changes to the Excel spreadsheet must be done to the file in Sharepoint. When a consistent set of changes is complete, copy the file into your working tree of this repo. Ensure the working tree is up to date with the remote reposisotry. Commit the file with a commit message of less than 80 characters. If more detail is needed, do so after a blank line in the message. Push the change to the repo and click the ***Reload System config*** button in the Web UI or send an reload command to the service via etcd. The etcd key being: /cmd/cfg.

The contents of the Excel spreadsheet will be converted to YAML and committed as the lwacfgsrv user. This file can be easily diff'd with git. It will also be pushed into Etcd under the key defined in key2fileMapping.yml. Subsystems can register callbacks on this key to dynamically update on changes.

The file: file2keyMapping.yml is critical to the functioning of the service.
It is of type: map[string]map[string]string where map is a key,val
dictionary. Top level keys are config filenames. Their associated map is for
the code responsible to convert this file into a YAML file and push the
contents to the distributed map(etcd). YAML files have the simplest form since
no conversion is needed. YAML file definitions are handled by the service so
the only work is to add the YAML file and provide the distributed map key to which it will be written to. See the example in file2keyMapping.yml.

The pythonMaster.py executable script is called by the service for any
additional config file conversions. The contents can be changed but the
input and return types must be adhered to. See the comment at the top of
the code. The script should ignore any files it is not resposible for like
direct pushing of YAML files. 

The service does perform a git pull prior to executing any code so changes will be incorporated using the standard Git workflow. 

