from flask import Blueprint, jsonify, send_file
import pandas as pd
from models import db, Product

report_bp = Blueprint('report', __name__)

@report_bp.route('/summary', methods=['GET'])
def summary():
    products = Product.query.all()
    data = [{
        'category': p.category,
        'total_revenue': p.price * p.quantity_sold,
        'product_name': p.product_name,
        'quantity_sold': p.quantity_sold
    } for p in products]

    df = pd.DataFrame(data)

    # Grouping and aggregating the data
    summary_df = df.groupby('category').agg({
        'total_revenue': 'sum',
        'quantity_sold': 'max'
    }).reset_index()

    # Rounding total_revenue to 2 decimal places and formatting
    summary_df['total_revenue'] = summary_df['total_revenue'].round(2).map(lambda x: f"{x:.2f}")

    # Adding top product names for each category
    summary_df['top_product'] = summary_df.apply(
        lambda row: df[(df['category'] == row['category']) & (df['quantity_sold'] == row['quantity_sold'])]['product_name'].values[0], 
        axis=1
    )

    # Renaming column for clarity
    summary_df.rename(columns={'quantity_sold': 'top_product_quantity_sold'}, inplace=True)

    summary_csv = './data/summary_report.csv'
    summary_df.to_csv(summary_csv, index=False)

    return send_file(summary_csv, as_attachment=True, download_name='summary_report.csv')
