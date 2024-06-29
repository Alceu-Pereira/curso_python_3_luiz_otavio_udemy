from datetime import datetime
from pytz import timezone

# data = datetime(2024, 6, 6, 11, 42, 22, 00, tzinfo=timezone('Asia/Tokyo'))

# data_str = '2024-06-28 11:44:08'
# data_str = '28/06/2024'
# # data_fmt = '%Y-%m-%d %H:%M:%S'
# data_fmt = '%d/%m/%Y'
# data = datetime.strptime(data_str, data_fmt)

data = datetime.now()


print(data.timestamp())
print(datetime.fromtimestamp(1719703629))