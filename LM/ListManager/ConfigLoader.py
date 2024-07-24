import yaml
import os

class ConfigLoader:
    def __init__(self, config_file):
        # Get the absolute path of the config file
        config_file_path = os.path.abspath(config_file)
        with open(config_file_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_message(self, key):
        return self.config['messages'].get(key, '')

    def get_path(self, key):
        path = self.config['paths'].get(key, '')
        return os.path.expanduser(path) if path else ''

# Load configuration from the correct path
config_loader = ConfigLoader('C:\\Users\\Asus\\Documents\\GitHub\\ListManager-Plugin\\LM\\Config\\config.yml')
