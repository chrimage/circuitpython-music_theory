import constants

class Interval:
    def __init__(self, interval_type: str, size: int):
        self.interval_type = constants.INTERVAL_TYPE_MAP[interval_type]
        self.size = size

    @classmethod
    def from_interval_string(cls, interval_string: str):
        interval_type = interval_string[0]
        size = int(interval_string[1:])
        return cls(interval_type, size)
