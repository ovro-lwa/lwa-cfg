#!/usr/bin/env python3

# pythonMaster.py is called by the lwacfg service to pull down, if necessary,
# any other known config files, convert them to YAML format, commit each one
# to the repo and push to the distributed map. pythonMaster.py is specifed
# in the file2keyMapping.yml file in this repo so can have any unique name.
# The service will do a one time
# push back to origin. The driving config file can be added to the repo
# manually if pulling can't be done. The service does a pull
# when launched so new code and config files can be added to the remote
# prior to commanding the service to 'reload'.
#
# This script should be written such that it can be executed from anywhere
# on the host.
#
# The code should return a non-zero error code on errors and any pertinent
# information.

import sys
import argparse

# constants
MAPPING_FILE = "/home/ubuntu/proj/lwa-shell/lwa-cfg/file2keyMapping.yml"
SUCCESS = 0

def eprint(*args, **kwargs):
    """ eprint writes to stderr
    """
    print(*args, file=sys.stderr, **kwargs)

def read_mapping_file():
    return {}

def process_config_files(file_map:dict):
    """process_config_files uses the file_map to define the YAML filename
to hold the conversion to YAML and the distributed map key to write to. Other
key,values can be added if needed to the file2mapping.yml file
    """

    for key, val_dict in file_map.items():
        # process
        pass

    # no errors
    return "", SUCCESS

def main_entry(upload:bool = False):
    """main_entry is the driver for all processing.
    """
    
    # Must read in 'files2Mapping.yml' file to know which files to process,
    # the output YAML file and the distributed map key to push to.
    file_mapping = read_mapping_file()

    if (upload):
        get_config_files()

    errmsg, errcode = process_config_files(file_mapping)

    if errcode != SUCCESS:
        print(errmsg)
        eprint(errcode)
    else:
        eprint(SUCCESS)

if __name__ == '__main__':

    # Mandatory argument.
    parser = argparse.ArgumentParser(description="Args")
    parser.add_argument('--upload', dest='upload', action='store_true')
    parser.set_defaults(upload=False)
    args = parser.parse_args()

    main_entry(args.upload)
