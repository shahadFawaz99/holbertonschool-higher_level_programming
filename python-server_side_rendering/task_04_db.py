from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        return None

def load_csv_data():
    try:
        data = []
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
        return data
    except Exception as e:
        return None

def load_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
    except Exception as e:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = load_json_data()
    elif source == 'csv':
        data = load_csv_data()
    elif source == 'sql':
        data = load_sql_data()
    else:
        error = 'Wrong source'
        return render_template('product_display.html', error=error)

    if data is None:
        error = 'Error loading data'
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = int(product_id)
            filtered_data = [item for item in data if item['id'] == product_id]
            if not filtered_data:
                error = 'Product not found'
            data = filtered_data
        except ValueError:
            error = 'Invalid ID format'
            data = []

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
