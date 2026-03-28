import os

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "AlphaWaveDB"
}

FREQ_BANDS = {
    "alpha": (8, 13),
    "beta": (13, 30)
}

DATA_PATH = os.path.join(os.path.dirname(__file__), "S001R01.edf")