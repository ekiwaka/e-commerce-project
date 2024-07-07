import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from models import db, Product

def load_csv_to_db(file_path):
    try:
        data = pd.read_csv(file_path)
        data.to_sql(name='product', con=db.engine, if_exists='append', index=False)
    except SQLAlchemyError as e:
        print(f"Error uploading data to database: {e}")
