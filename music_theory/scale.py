class Scale:
    _MAJOR = ('M2', 'M3', 'P4', 'P5', 'M6', 'M7', 'P8')
    _HARMONIC_MINOR = ('M2', 'm3', 'P4', 'P5', 'm6', 'M7', 'P8')
    _NATURAL_MINOR = ('M2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8')
    _MELODIC_MINOR = ('M2', 'm3', 'P4', 'P5', 'M6', 'M7', 'P8')
    _DORIAN = ('M2', 'm3', 'P4', 'P5', 'M6', 'm7', 'P8')
    _LOCRIAN = ('m2', 'm3', 'P4', 'dim5', 'm6', 'm7', 'P8')
    _LYDIAN = ('M2', 'M3', 'aug4', 'P5', 'M6', 'M7', 'P8')
    _MIXOLYDIAN = ('M2', 'M3', 'P4', 'P5', 'M6', 'm7', 'P8')
    _PHRYGIAN = ('m2', 'm3', 'P4', 'P5', 'm6', 'm7', 'P8')
    _MAJOR_PENTATONIC = ('M2', 'M3', 'P5', 'M6', 'P8')
    _MINOR_PENTATONIC = ('m3', 'P4', 'P5', 'm7', 'P8')
    _CHROMATIC = ('m2', 'M2', 'm3', 'M3', 'P4', 'aug4', 'P5', 'm6', 'M6', 'm7', 'M7', 'P8')
    _SCALE_PATTERNS = {
        'major': _MAJOR,
        'maj': _MAJOR,
        'minor': _HARMONIC_MINOR,
        'min': _HARMONIC_MINOR,
        'natural minor': _NATURAL_MINOR,
        'nat min': _NATURAL_MINOR,
        'melodic minor': _MELODIC_MINOR,
        'dorian': _DORIAN,
        'locrian': _LOCRIAN,
        'lydian': _LYDIAN,
        'mixolydian': _MIXOLYDIAN,
        'phrygian': _PHRYGIAN,
        'major pentatonic': _MAJOR_PENTATONIC,
        'minor pentatonic': _MINOR_PENTATONIC,
        'chromatic': _CHROMATIC
    }

    @classmethod
    def build_scale(cls, tonic, scale_type):
        # code omitted for brevity

        scale = [tonic]
        for diff in scale_pattern:
            new = (scale[0] + Interval.from_interval_string(diff))
            scale.append(new)
        return scale
