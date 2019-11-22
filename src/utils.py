from datetime import datetime, timedelta


def time_stamp():
    return str((datetime.now() - timedelta(hours=2)).strftime("%Y%m%d%H%M%S"))
