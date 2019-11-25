from datetime import datetime, timedelta
from src.constants import DATA_DAILY


def time_stamp(implicit=False):
    if implicit:
        return str(datetime.now().strftime("%Y%m%d"))
    return str((datetime.now() - timedelta(hours=2)).strftime("%Y%m%d%H%M%S"))


def write_all_matches_ids(date, data):

    with open(DATA_DAILY + date, 'w') as of:
        of.write(str(len(data)) + '\n')
        for line in data:
            of.write(line['Match'] + '\n')
