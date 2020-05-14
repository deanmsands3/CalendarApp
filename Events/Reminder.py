from .Override import Override
from typing import List


class Reminder(object):
    _use_default: bool  # boolean
    _overrides: list    # array(Override)

    def __init__(self, useDefault: bool, overrides: List[Override]):
        self._use_default = useDefault
        self._overrides = overrides

    @property
    def useDefault(self) -> bool:
        return self._use_default

    @useDefault.setter
    def useDefault(self, value: bool):
        self._use_default = value

    @property
    def overrides(self) -> List[Override]:
        return self._overrides

    @overrides.setter
    def overrides(self, value: List[Override]):
        self._overrides = value
