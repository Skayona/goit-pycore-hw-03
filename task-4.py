from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
  """
  The list of users to congratulate.

  :param users: a list of users data: `name` and `birthday` in format `YYYY.MM.DD`.

  :return: list of users whose birtday is in 7 days (including today) in the follwing
            format: `name` and `congratulation_date` in format `YYYY.MM.DD`.
            If the birthday is on weekend, the congratulation is sent on weekday.

  """

  today = datetime.today().date()
  # today = datetime(2026, 10, 19).date() #For testing edge cases
  date_str_format = '%Y.%m.%d'
  congratulation_list = []

  for user in users:
    users_bd = datetime.strptime(user["birthday"], date_str_format).date()
    birthday_this_year = handle_leap_year(users_bd, today.year)

    should_notify_next_year = today.weekday() == 0 and (today - birthday_this_year).days > 2 or today.weekday() > 0 and  birthday_this_year < today

    if should_notify_next_year:
      birthday_this_year = handle_leap_year(users_bd, today.year + 1)

    diff = (birthday_this_year - today).days

    if diff < 7:
      birthday_weekday = birthday_this_year.weekday()

      if (birthday_weekday >= 5):
        first_weekday = 7 - birthday_weekday
        birthday_this_year += timedelta(days=first_weekday)

      congratulation_list.append({
        "name": user["name"],
        "congratulation_date": birthday_this_year.strftime( date_str_format)
      })

  return congratulation_list

def handle_leap_year(date: datetime.date, year: int) -> datetime.date:
  """
  Handles cases when the birthday is on the 29th of Feb.
  For non leap years sets the date as the 1st of Mar.
  """
  try:
    return date.replace(year=year)
  except ValueError:
    return date.replace(year=year, month=3, day=1)


users = [ {"name": "John Doe", "birthday": "1985.10.23"}, {"name": "Jane Smith", "birthday": "1990.10.25"}, {"name": "Alisa Parker", "birthday": "2000.10.15"}, {"name": "Carl Forest", "birthday": "1985.10.17"}, {"name": "Arthur Scott", "birthday": "1999.10.31"}]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
