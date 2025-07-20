from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception:
        return []

def read_csv():
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            return [dict(row) for row in reader]
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    data = []

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    # Convert id to integer if exists and valid
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            error = "Invalid product ID"
            return render_template("product_display.html", error=error)

        filtered = [item for item in data if int(item.get("id", -1)) == product_id]
        if not filtered:
            error = "Product not found"
            return render_template("product_display.html", error=error)
        data = filtered

    return render_template("product_display.html", products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
