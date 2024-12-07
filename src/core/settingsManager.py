from typing import Any
from colorama import Fore
from core.logger import Logger
import json


class SettingsManager:
    def __init__(self, settings_file: str) -> None:
        self.file = settings_file
        self._settings_dict = {}

        self.logger = Logger("Settings Manager")

        self._load_settings()
    
    def _load_settings(self) -> None:
        try:
            with open(self.file, "r") as file:
                self._settings_dict = json.load(file)
        except FileNotFoundError:
            self.logger.error(f"Could not find settings file: '{self.file}'")
            exit(0)
        
        self.logger.log("Successfully loaded settings")
    
    def save_settings(self) -> None:
        json_obj = json.dumps(self._settings_dict, indent=4)
        self.logger.log("Saving settings...")

        try:
            with open(self.file, "w") as file:
                file.write(json_obj)
            self.logger.log("Saved settings")
        except:
            self.logger.warning("Could not save settings")
        
    
    def _internal_load_setting(self, setting_name: str) -> None:
        #* Do not directly use outside of class
        steps = setting_name.split(".")
        setting = self._settings_dict[steps.pop(0)]

        try:
            for step in steps:
                setting = setting[step]
        except KeyError:
            self.logger.error(f"Setting not found: {setting_name}")
            exit()
        
        return setting
    
    def read_setting(self, setting_name: str) -> Any:
        return self._internal_load_setting(setting_name)
    
    def change_setting(self, setting_name: str, value: Any) -> None:
        steps = setting_name.split(".")
        old_value: Any = self._internal_load_setting(setting_name)

        setting = self._internal_load_setting(".".join(steps[:-1]))
        setting[steps[-1]] = value

        self.logger.log(f"Changed setting {setting_name} from {old_value} to {value}")