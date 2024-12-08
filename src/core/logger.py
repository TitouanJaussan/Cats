from colorama import Fore


class Logger:
    def __init__(self, name: str) -> None:
        self.name = name

        self._error_colors = [Fore.RESET, Fore.YELLOW, Fore.RED]
        self._BOLD = "\033[1m"
        self._END = "\033[0m"

    def _internal_log(self, msg: str, error_level: int = 0):
        msg = f"{self._BOLD}[{self.name}]{self._END}: {msg}"

        msg = self._error_colors[min(max(error_level, 0), 2)] + msg

        print(msg, end="\n" + Fore.RESET)

    def log(self, msg: str) -> None:
        self._internal_log(msg, 0)

    def warning(self, msg: str) -> None:
        self._internal_log("Warning: " + msg, 1)

    def error(self, msg: str) -> None:
        self._internal_log("Error: " + msg, 2)
