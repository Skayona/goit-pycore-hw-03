import re

def normalize_phone(phone_number: str) -> str:
  '''
    Sanitizes the provided phone number and returns it in the valid format.


    :param phone_number: string, phone number in various formats
    :return: string,sanitized phone number in format `+380123456789`
  '''

  regex = r'[^+\d]'

  phone_num = re.sub(regex, '', phone_number)

  if (phone_num.startswith('380')):
    return f'+{phone_num}'

  if (phone_num.startswith('80')):
    return f'+3{phone_num}'

  if (phone_num.startswith('0')):
    return f'+38{phone_num}'

  return phone_num




# raw_numbers = [ "067\t123 4567", "(095) 234-5678\n", "+380 44 123 4567", "380501234567", " +38(050)123-32-34", " 0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11 "]
# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Normalized phone numbers for SMS mailing list:", sanitized_numbers)

# Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']