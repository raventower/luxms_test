from api import APIRequests
from etl import ETLProcesser
import pandas as pd
import requests
import sqlalchemy
import json


# Запуск ETL процесса с целью получения необходимой витрины данных
etl = ETLProcesser()
answer = etl.earth_by_mounth()
print(answer)

# Формирование и препроцессинг дата фрейма с данными от API
df = pd.DataFrame(answer[1], index=answer[0], columns=['num_of_earth'])
df.index = pd.to_datetime(df.index)
df.index.name='air_date'
df

# Загрузка данных в sqlite3 базу данных
engine = sqlalchemy.create_engine('sqlite:///sqlite3.db', echo=False)
df.to_sql('earth_characters', con=engine, if_exists='replace')