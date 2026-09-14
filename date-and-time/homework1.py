import datetime

x = datetime.datetime.now()
print(x)

from datetime import datetime
import pytz

tz_india = pytz.timezone("Asia/Kolkata")
datetime_india = datetime.now(tz_india)

print("India time:", datetime_india.strftime("%H:%M:%S"))