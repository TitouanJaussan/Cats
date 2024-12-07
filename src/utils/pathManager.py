import os
from platform import system


class PathManager:
    def __init__(self, main_script_path: str) -> None:
        self.os = system()
        self.separator = self._get_default_separator()
        self.path = os.path.abspath(main_script_path)
        self.path = self.separator.join(self.path.split(self.separator)[:-2])
        self.chdir()

    def _get_default_separator(self) -> str:
        return "\\" if self.os.lower() == "windows" else "/"

    def chdir(self) -> None:
        os.chdir(self.path)

    def concatenate(self, *args) -> str:
        return self.separator.join(args)
    
    def get_extension(self, file_name: str) -> str:
        return file_name[::-1][:file_name[::-1].index(".")][::-1]
    
    def matches_extension(self, file_name: str, extension: str) -> bool:
        return self.get_extension(file_name) == extension

    def remove_extension(self, file_name: str, extension: str) -> str:
        return file_name[:file_name.index(extension) - 1]