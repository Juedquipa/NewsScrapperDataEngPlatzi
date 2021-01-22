import yaml


def config():
    __config = None
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.safe_load(f)

            return __config
