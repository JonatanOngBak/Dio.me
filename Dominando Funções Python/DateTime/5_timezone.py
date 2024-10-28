from datetime import datetime, timezone, timedelta

# se tratando de OSLO temos +2 horas
data_Oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_Oslo)
print(data_sao_paulo)