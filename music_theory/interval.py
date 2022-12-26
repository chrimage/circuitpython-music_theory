class Interval:
    NAMED_INTERVAL_TYPES = ('M', 'm', 'P', 'dim', 'aug')
    VALID_INTERVAL_TYPES = ('dim1', 'P1', 'aug1', 'dim2', 'm2', 'aug2', 'M2', 'dim3', 'm3', 'M3', 'aug3', 'dim4', 'P4', 'aug4', 'dim5', 'P5', 'aug5', 'dim6', 'm6', 'M6', 'aug6', 'dim7', 'm7', 'M7', 'aug7')
    _PERFECT_INTERVALS_SEMITONES = {1: 0, 4: 5, 5: 7}
    _MAJOR_INTERVALS_SEMITONES = {2: 2, 3: 4, 6: 9, 7: 11}

    def __init__(self, interval_type, size):
        if not isinstance(interval_type, str):
            raise TypeError(f"Expected string for interval type, got '{interval_type}'")
        if interval_type not in Interval.NAMED_INTERVAL_TYPES:
            raise ValueError(f"Unsupported interval type specified: {interval_type}")
        if not isinstance(size, int):
            raise TypeError(f"Expected integer for interval distance, got: {size}")
        if size <= 0:
            raise ValueError(f"Expected interval distance to be positive, got: {size}")
        interval_string = f"{interval_type}{size}"
        if interval_string not in Interval.VALID_INTERVAL_TYPES:
            raise ValueError(f"Impossible interval type specified: {interval_type}{size}")
        self.interval_type = interval_type
        self.size = size

    @classmethod
    def from_interval_string(cls, interval_string):
        if not isinstance(interval_string, str):
            raise TypeError(f"Expected string for interval string, got '{interval_string}'")
        for i in Interval.NAMED_INTERVAL_TYPES:
            if interval_string.startswith(i):
                interval_type = i
                size = interval_string.replace(i, '')
                return cls(interval_type, size)
        raise ValueError(f"Invalid interval string: {interval_string}")

    def __str__(self):
        return f"{self.interval_type}{self.size}"

_TONE = Interval.from_interval_string('M2')
_SEMITONE = Interval.from_interval_string('m2')
_TONE_AND_HALF = Interval.from_interval_string('aug2')
