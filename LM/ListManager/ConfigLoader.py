import yaml

class ConfigLoader:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def get_message(self, key):
        return self.config.get('messages', {}).get(key, "Message not found")

    def get_path(self, key):
        return self.config.get('paths', {}).get(key, "Path not found")

    def get_help_guide(self):
        return self.config.get('help-guide', [])
