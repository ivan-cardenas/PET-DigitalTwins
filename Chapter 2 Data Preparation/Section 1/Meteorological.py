!pip install knmy

from datetime import datetime, timedelta
import pandas as pd
today = datetime.now()
yesterday = datetime.today() - timedelta(days=365)
today= today.strftime("%Y%m%d%H")
yesterday= yesterday.strftime("%Y%m%d%H")
print(yesterday)
print(today)

from knmy import knmy
disclaimer, stations, variables, data = knmy.get_knmi_data(type='hourly',stations=[290], start=2019072700, end= 2019072800,
                                                             inseason=False, variables=['SUNR'], parse=True)
print(stations)
print(variables)

pd.DataFrame(data)
