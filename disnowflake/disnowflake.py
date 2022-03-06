from datetime import datetime


def snow_date(id: int) -> list:
    """Convert the snowflake ID to a date

    Parameters
    ----------
    id : int
        The ID of the snowflake

    Returns
    -------
        A list of the year, month, day, hour, minute, second, and microsecond of the snowflake.

    """
    stamp_bin = bin(id >> 22)
    stamp_dec = int(stamp_bin, 0)
    stamp_to_unix = (stamp_dec + 1420070400000) / 1000
    timestamp = datetime.fromtimestamp(t=stamp_to_unix)
    now = list()
    now.append(timestamp.year)
    now.append(timestamp.month)
    now.append(timestamp.day)
    now.append(timestamp.hour)
    now.append(timestamp.minute)
    now.append(timestamp.second)
    now.append(timestamp.microsecond)
    return now
