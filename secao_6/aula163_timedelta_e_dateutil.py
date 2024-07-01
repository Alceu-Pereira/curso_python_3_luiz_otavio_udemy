from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('30/06/2024 09:01:49', fmt)
# print(data_inicio > data_fim)
# delta = data_fim - data_inicio
# print(delta)
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# delta = timedelta(days=10, hours=2)
# print(data_fim + delta)
# print(data_fim + relativedelta(days=10, hours=2, seconds=60))

delta = relativedelta(data_fim, data_inicio)
print(delta)