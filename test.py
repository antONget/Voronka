# from datetime import datetime
# now = datetime.now()
# current_time = now.strftime("%H")
# print("Current Time =", current_time)

import datetime
now = datetime.datetime.now()
time_22 = now.replace(hour=22, minute=0, second=0, microsecond=0)
time_10 = now.replace(hour=10, minute=0, second=0, microsecond=0)
print(now > time_22 or now < time_10)    # Если сейчас больше 16:00 будет True

