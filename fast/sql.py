from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd

engine = create_engine(os.getenv('POSTGRES_LINK'))

Session = sessionmaker(bind=engine)

def get_avg_price(city):
    query = text(f"select AVG(room_price) from airbnb where city='{city}' GROUP BY city")
    df = pd.read_sql_query(query, engine).values[0][0]
    return df

def get_avg_satisfaction(city):
    query = text(f"select AVG(satisfaction) from airbnb where city='{city}' GROUP BY city")
    df = pd.read_sql_query(query, engine).values[0][0]
    return df

if __name__=='__main__':
    city = 'barcelona'
    print(f'Average satisfaction score for {city} is {round(get_avg_satisfaction(city),2)} %')
    print(f'Average room price for {city} is €{round(get_avg_price(city),2)}')
    