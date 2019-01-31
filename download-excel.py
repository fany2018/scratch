import ssl
import pandas as pd
import datetime

ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_excel('https://www.nationalgridgas.com/sites/gas/files/documents/ST%20' + datetime.datetime.now().strftime("%d.%m.%Y") + '.xls', sheet_name='Today')

print("Column headings:")
print(df.columns)
