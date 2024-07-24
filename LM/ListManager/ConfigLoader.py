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

# Load configuration
config_loader = ConfigLoader(os.path.join(os.path.dirname(__file__), 'config.yml'))

# Get the new data path
data_path = config_loader.get_path('data_folder')
print(f"Data path: {data_path}")
