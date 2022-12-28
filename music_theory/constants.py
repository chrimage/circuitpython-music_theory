NAMED_INTERVAL_TYPES = ('M', 'm', 'P', 'dim', 'aug')
VALID_INTERVAL_TYPES = ('dim1', 'P1', 'aug1', 'dim2', 'm2', 'aug2', 'M2', 'dim3', 'm3', 'M3', 'aug3', 'dim4', 'P4', 'aug4', 'dim5', 'P5', 'aug5', 'dim6', 'm6', 'M6', 'aug6', 'dim7', 'm7', 'M7', 'aug7')
VALID_PITCHES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
VALID_ACCIDENTALS = ('#', '##', 'b', 'bb', None)
ACCIDENTAL_MAP = {'#': 'sharp', '##': 'double sharp', 'b': 'flat', 'bb': 'double flat'}
PITCH_ACCIDENTAL_MAP = {'C#': ('C', '#'), 'C##': ('C', '##'), 'Db': ('D', 'b'), 'Dbb': ('D', 'bb'), 'D#': ('D', '#'), 'D##': ('D', '##'), 'Eb': ('E', 'b'), 'Ebb': ('E', 'bb'), 'F#': ('F', '#'), 'F##': ('F', '##'), 'Gb': ('G', 'b'), 'Gbb': ('G', 'bb'), 'G#': ('G', '#'), 'G##': ('G', '##'), 'Ab': ('A', 'b'), 'Abb': ('A', 'bb'), 'A#': ('A', '#'), 'A##': ('A', '##'), 'Bb': ('B', 'b'), 'Bbb': ('B', 'bb'), 'B#': ('B', '#'), 'B##': ('B', '##')}
SCALE_TYPE_MAP = {
    'major': ('major', 'maj', 'ionian', 'ion', '1'),
    'minor': ('minor', 'min', 'aeolian', 'aeo', '6'),
    'natural minor': ('natural minor', 'nat min', 'natural aeolian', 'nat aeo', '6'),
    'melodic minor': ('melodic minor', 'mel min', 'melodic', 'mel', 'melodic 6'),
    'dorian': ('dorian', 'dor', '2'),
    'locrian': ('locrian', 'loc', '7'),
    'lydian': ('lydian', 'lyd', '3'),
    'mixolydian': ('mixolydian', 'mix', '4'),
    'phrygian': ('phrygian', 'phr', '5'),
    'major pentatonic': ('major pentatonic', 'maj pent', 'pentatonic', 'pent', 'major pent'),
    'minor pentatonic': ('minor pentatonic', 'min pent', 'minor pent'),
    'chromatic': ('chromatic', 'chrom'),
}

CHORD_TYPE_MAP = {
    'major': (4, 3),
    'minor': (3, 4),
    'dim': (3, 3),
    'aug': (4, 4),
    'dom7': (4, 3, 3),
    'maj7': (4, 3, 4),
    'min7': (3, 4, 3),
    'hdim7': (3, 3, 3),
    'minmaj7': (3, 4, 4),
    'maj6': (4, 3, 2),
    'min6': (3, 4, 2),
    '9': (4, 3, 3, 4),
    'maj9': (4, 3, 4, 4),
    'min9': (3, 4, 3, 4),
    'sus2': (2, 5, 5),
    'sus4': (5, 2, 5)
}

CHORD_NUM_SCALE_INDEX = {'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4, 'VI': 5, 'VII': 6, 'VIII': 7}

VALID_PITCHES = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
VALID_ACCIDENTALS = ('#', '##', 'b', 'bb', None)
MAJOR_SCALE_INTERVALS = (2, 2, 1, 2, 2, 2, 1)
NATURAL_MINOR_SCALE_INTERVALS = (2, 1, 2, 2, 1, 2, 2)
HARMONIC_MINOR_SCALE_INTERVALS = (2, 1, 2, 2, 1, 3, 1)
MELODIC_MINOR_SCALE_ASCENDING_INTERVALS = (2, 1, 2, 2, 2, 2, 1)
MELODIC_MINOR_SCALE_DESCENDING_INTERVALS = (1, 2, 2, 1, 2, 2, 2)
CHROMATIC_SCALE_INTERVALS = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
INTERVAL_TYPE_MAP = {
    "P": 0,
    "m": 1,
    "M": 2,
    "aug": 3,
    "dim": -2,
    "M2": 2,
    "m2": 1,
    "aug2": 3,
    "dim2": -2,
    "M3": 4,
    "m3": 3,
    "aug3": 5,
    "dim3": -1,
    "P4": 5,
    "aug4": 6,
    "dim4": -1,
    "P5": 7,
    "aug5": 8,
    "dim5": -1,
    "M6": 9,
    "m6": 8,
    "aug6": 10,
    "dim6": -1,
    "M7": 11,
    "m7": 10,
    "aug7": 12,
    "dim7": -1,
    "P8": 12,
}
ACCIDENTAL_MAP = {
    "#": 1,
    "##": 2,
    "b": -1,
    "bb": -2,
    "": 0,
}

PITCH_ACCIDENTAL_MAP = {
    "C#": ("C", "#"),
    "D#": ("D", "#"),
    "E#": ("E", "#"),
    "F#": ("F", "#"),
    "G#": ("G", "#"),
    "A#": ("A", "#"),
    "B#": ("B", "#"),
    "Cb": ("C", "b"),
    "Db": ("D", "b"),
    "Eb": ("E", "b"),
    "Fb": ("F", "b"),
    "Gb": ("G", "b"),
    "Ab": ("A", "b"),
    "Bb": ("B", "b"),
    "C##": ("C", "##"),
    "D##": ("D", "##"),
    "E##": ("E", "##"),
    "F##": ("F", "##"),
    "G##": ("G", "##"),
    "A##": ("A", "##"),
    "B##": ("B", "##"),
    "Cbb": ("C", "bb"),
    "Dbb": ("D", "bb"),
    "Ebb": ("E", "bb"),
    "Fbb": ("F", "bb"),
    "Gbb": ("G", "bb"),
    "Abb": ("A", "bb"),
    "Bbb": ("B", "bb"),
}

