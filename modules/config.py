import json


def get_config(config_path: str) -> dict:
    config = dict()

    try:
        with open(config_path) as conf:
            config = dict(json.load(conf))
    except:
        print("Could not read the config file.")

    return config
