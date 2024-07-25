import yaml
import os

class ConfigLoader:
    def __init__(self, config_file):
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"{config_file} does not exist.")
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)

    def get_path(self, key):
        path = self.config['paths'].get(key, '')
        # Make the path relative to the script's location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, path)
        path = os.path.expanduser(path)  # Expand ~ to home directory
        return os.path.abspath(path)     # Convert to absolute path

    def get_message(self, key):
        return self.config['messages'].get(key, '')



# Example usage
config_loader = ConfigLoader(r'C:\Users\Asus\Documents\GitHub\ListManager-Plugin\LM\Config\config.yml')

