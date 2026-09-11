print("""
****************************
DateTime Module
****************************
""")
from datetime import datetime

import locale

locale.setlocale(locale.LC_ALL,"")


now = datetime.now()

print(datetime.ctime(now))

print(now.year)

print(now.month)

print(now.hour, ":" ,now.minute, ":", now.second)

print(datetime.strftime(now,  "%B"))

print(datetime.strftime(now,  "%Y"))

print(datetime.strftime(now,  "%A"))

print(datetime.strftime(now,  "%D %B %Y %A"))





now = datetime.now()

saniye = datetime.timestamp(now)

print(saniye)

now2 = datetime.fromtimestamp(saniye)

print(now2)




now = datetime.fromtimestamp(0)

print(now)


birth_date = datetime(2010, 9, 18)

now = datetime.now()

print("Time passed since birthday:", birth_date - now)

