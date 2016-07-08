# import json

class ConfigAppSystem:

    fileConfigured = ""

    def load_config_file(self):

        config_file = open("application/config.txt", "r").read()

        # fileConfigured = config_file['fileConfigured']
        # print(config_file)

    def __init__(self):
        super().__init__()
        self.load_config_file()
