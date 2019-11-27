from datetime import datetime, timedelta


def time_stamp(implicit=False):
    if implicit:
        return datetime.now().strftime("%Y%m%d")
    return (datetime.now() - timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
