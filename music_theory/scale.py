from .note import Note
from .interval import Interval
from .constants import SCALE_TYPE_MAP

class Scale(object):
    @classmethod
    def build_scale(cls, tonic, scale_type):
        if not isinstance(tonic, Note):
            raise TypeError(f"Expected Note for tonic, got {tonic}")
        if not isinstance(scale_type, str):
            raise TypeError(f"Expected string for scale type, got {scale_type}")
        if scale_type not in SCALE_TYPE_MAP:
            raise ValueError(f"Unknown scale type: {scale_type}")

        intervals = SCALE_TYPE_MAP[scale_type]
        scale = [tonic]
        for diff in intervals:
            new = scale[0] + Interval.from_interval_string(diff)
            scale.append(new)
        return scale

