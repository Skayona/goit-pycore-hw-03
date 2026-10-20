from datetime import datetime

def get_days_from_today(date: str) -> int | None:
  """
  Calculates the number of days between the current date and a specified date.

  :param date: string in `YYYY-MM-DD` format
  :return: integer representing the difference between today and the specified date
            (negative if the specified date is in the future).
            Returns `None` if the specified date format is invalid.
  """

  date_str_format = '%Y-%m-%d'

  try:
    date_obj = datetime.strptime(date, date_str_format)
  except ValueError:
    print(f'Invalid date format. Please use YYYY-MM-DD format.')
    return None
  except TypeError:
    print(f'Provided value is not a date. Please provide a date in YYYY-MM-DD format.')
    return None

  today = datetime.today()

  return today.toordinal() - date_obj.toordinal()

# print(get_days_from_today('2026-12-31')) #-74
# print(get_days_from_today('2026-01-01')) #290
# print(get_days_from_today('23-12-31')) # Invalid date format: time data '23-12-31' does not match format '%Y-%m-%d'. Please use YYYY-MM-DD format. None
# print(get_days_from_today(1)) # Invalid date format: strptime() argument 1 must be str, not int. Please use YYYY-MM-DD format. None