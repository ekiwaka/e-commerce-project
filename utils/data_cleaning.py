import pandas as pd

def clean_data(df):
    # Fill missing values
    df['price'] = df['price'].fillna(df['price'].median())
    df['quantity_sold'] = df['quantity_sold'].fillna(df['quantity_sold'].median())

    def fill_rating(row):
        if pd.isna(row['rating']):
            category = row['category']
            avg_rating = df[df['category'] == category]['rating'].mean()
            return avg_rating
        return row['rating']

    df['rating'] = df.apply(fill_rating, axis=1)

    # Ensure numeric types
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['quantity_sold'] = pd.to_numeric(df['quantity_sold'], errors='coerce')
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    return df
