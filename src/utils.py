from datetime import datetime
import pytz


def timestamp_to_datetime(timestamp):
    dt = datetime.fromtimestamp(int(timestamp / 1000), pytz.timezone('UTC'))
    return dt.isoformat().split('+')[0] + 'Z'  # Z for Zulu timezone (UTC)


def datetime_now():
    return datetime.now(pytz.timezone('UTC')).isoformat().split('+')[0] + 'Z'  # Z for Zulu timezone (UTC)