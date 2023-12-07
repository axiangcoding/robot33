from enum import Enum


class CommonError(Enum):
    SUCCESS = (0, "success")
    ERROR = (1000, "internal error")

    @property
    def code(self):
        return self.value[0]

    @property
    def description(self):
        return self.value[1]
