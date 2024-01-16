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
class YamlRead:

    def __init__(self, config_path):
        self.file_path = config_path
        file_path = 'config.yaml'

        if config_path is None:
            current_path = os.path.join(os.getcwd(), 'config')
            self.file_path = os.path.join(current_path, file_path)

        else:
            current_path = os.path.join(config_path, 'config')
            self.file_path = os.path.join(current_path, file_path)


        with open(self.file_path, 'r', encoding="UTF-8", errors='ignore') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def get_data(self):
        return self.data


def get(key, config_path):
    data = YamlRead(config_path).get_data()
    return data.get('config').get(key, None)

