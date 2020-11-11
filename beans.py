import sqlalchemy as db
import pandas as pd
import matplotlib.pyplot as plt
engine = db.create_engine('mysql+pymysql://root:@localhost:3306/application')

df = pd.read_csv('items.csv')




