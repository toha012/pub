from src.log import LOG_LEVEL

class Context():
    def __init__(self) -> None:
        self.log_level = LOG_LEVEL.INFO

context = Context()