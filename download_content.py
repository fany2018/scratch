
import requests
data_params = {'PublicationObjectIds': '413:4253,413:4267,413:10194,413:10097,413:13513,413:13516,413:13540', 'Applicable': 'applicableAt','FromUtcDatetime':'2019-01-10T00:00:00.000Z','ToUtcDateTime':'2019-01-16T00:00:00.000Z','FileType':'Csv'}
response = requests.post("http://mip-prod-web.azurewebsites.net/DataItemViewer/DownloadFile", params=data_params)
print response.content
open('website_data.csv', 'wb').write(response.content)
