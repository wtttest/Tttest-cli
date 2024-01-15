import os

import yaml


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class YamlReader:
    def __init__(self, config_path):
        self.file_path = config_path
        current_path = os.path.join(os.getcwd(), 'config') #os.path.dirname(os.path.abspath(__file__))

        if config_path is None:
            file_path = 'config.yaml'
            self.file_path = os.path.join(current_path, file_path)
        env_name = os.getenv("ENV_NAME")
        if env_name is not None:
            file_path = f'config-{env_name}.yaml'
            self.file_path = os.path.join(current_path, file_path)

        with open(self.file_path, 'r', encoding="UTF-8") as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_data(self):
        return self.data


def get(key, config_path):
    data = YamlReader(config_path).get_data()

    return data.get('config').get(key, None)
