import hashlib
from datetime import datetime, timedelta

from src.dev_creds import AUTH_KEY, DEV_ID


def time_stamp():
    return str((datetime.now() - timedelta(hours=2)).strftime("%Y%m%d%H%M%S"))


def make_signature(endpoint):
    sig = DEV_ID + endpoint + AUTH_KEY + time_stamp()
    return hashlib.md5(sig.encode('utf-8')).hexdigest()
