import ssl
import pandas as pd
from datetime import date, timedelta

ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_excel('https://www.nationalgridgas.com/sites/gas/files/documents/ST%20' + date.today().strftime("%d.%m.%Y") + '.xls', sheet_name='Today')

print(df)

df2 = pd.read_csv('https://www.interconnector.com/Data/ISIS/flowdata/interconnector_historical_' + date.today().strftime("%Y%m") + '.txt')
print(df2[df2['Gasday']==(date.today() - timedelta(1)).strftime("%d/%m/%Y")])
