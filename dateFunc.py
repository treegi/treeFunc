from typing import List, Dict, Union 
from datetime import date, datetime, timedelta
from dateutil.rrule import rrule, DAILY, MONTHLY

def date_range(start_date, end_date):
    return [dt.date() for dt in rrule(DAILY, dtstart=start_date, until=end_date)]

def month_range(start_date, end_date):
    return [dt.date() for dt in rrule(MONTHLY, dtstart=start_date, until=end_date)]

def season_range(start_date, end_date):

    if isinstance(start_date, datetime):
        start_date = start_date.date()

    if isinstance(end_date, datetime):
        end_date = end_date.date()

    ret = []
    for year in range(start_date.year-1, end_date.year+1):
        ret += [date(year, 5, 15),
                date(year, 8, 14),
                date(year, 11, 14),
                date(year+1, 3, 31)]
    ret = [r for r in ret if start_date < r < end_date]

    return ret

from iterFunc import pairwise

def splitDatetimeMonth(start_datetime : datetime, end_datetime : datetime, part_size = 100) -> List[datetime]:
    """splite datetime to formal size

    Args:
        start_datetime (datetime): start datetime
        end_datetime (datetime): end datetime
        part_size (int, optional): size of part. Defaults to 100.

    Returns:
        List[datetime]: datetime list
    """
    day = end_datetime - start_datetime
    day_splite = day.days / part_size
    day_splite_list =[start_datetime]

    for d_s in range(int(day_splite)):
        start_datetime = start_datetime + timedelta(days = part_size)
        day_splite_list.append(start_datetime)
        
    day_splite_list.append(end_datetime)
    return day_splite_list