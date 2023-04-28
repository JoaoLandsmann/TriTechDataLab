import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost:5000/db_site}')
      
query = "SELECT * FROM bibliotecas;"
 
df2 = pd.read_sql(query, engine)
print(df2.head())