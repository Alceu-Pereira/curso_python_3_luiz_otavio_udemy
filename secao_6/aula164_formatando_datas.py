from datetime import datetime

fmt = '%d%m%Y'
data = datetime.strptime('2024-6-30 21:11:29', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%Y'))
print(data.strftime('%Y'), data.year)
