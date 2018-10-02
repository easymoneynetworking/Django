from datetime import datetime , timedelta
dt_now = datetime.now()
delta_days = timedelta(days=1)
delta_month = timedelta(days=365/12)

print('Сегодня:' , dt_now.srtftime('%d,$m,%Y'))
print('Вчера:' , (dt_now - delta.days).srtftime('%d,%m,$Y'))
print('Месяц назад:' , (dt_now - delta_month).strftime('%d,%m,%Y'))