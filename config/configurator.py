#!/usr/bin/python2

import yaml
import os
import sys


def assert_file_exists_and_write_yaml(filename, yamldata):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != exc.errno.EEXIST:
                raise

    with open(filename, "w") as f:
        f.write(yaml.dump(yamldata, default_flow_style=False))


def get_config_yaml_data():
    data_path = os.environ.get('SNAP_APP_DATA_PATH')
    app_path = os.environ.get('SNAP_APP_PATH')

    if not data_path or not app_path:
        print('$SNAP_APP_DATA_PATH or $SNAP_APP_PATH is not defined')
        sys.exit(1)

    config_path = os.path.join(data_path, 'config', 'config.yaml')
    data = None
    if os.path.isfile(config_path):
        with open(config_path, 'r') as f:
            data = yaml.load(f)
    else:
        # no config written yet. Take default and write it in data path
        with open(os.path.join(app_path, 'config', 'default_config.yaml'), 'r') as f:
            data = yaml.load(f)
        assert_file_exists_and_write_yaml(config_path, data)
    return data


def print_current_config():
    data = get_config_yaml_data()
    print(yaml.dump(data, default_flow_style=False))


def set_new_config(newdata):
    data_path = os.environ.get('SNAP_APP_DATA_PATH')
    config_path = os.path.join(data_path, 'config', 'config.yaml')
    data = yaml.load(newdata)
    # no checks for now, simply write the new config
    assert_file_exists_and_write_yaml(config_path, data)


def retrieve_config_val(key):
    data = get_config_yaml_data()

    try:
        val = data['config']['ethereum'][key]
    except:
        print("Could not find key {} in the configuration file".format(key))
        sys.exit(1)

    print(val)


if __name__ == "__main__":
    input_bytes = sys.stdin.read()
    if len(input_bytes) != 0:
        set_new_config(input_bytes)
    else:
        print_current_config()
