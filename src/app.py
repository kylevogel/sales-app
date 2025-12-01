import logging
import sys
from prometheus_client import start_http_server, Counter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("sales-app")

APP_STARTS = Counter('app_startups_total', 'Total number of times the app has started')
APP_STARTS.inc()

try:
    start_http_server(9090)
    logger.info("Metrics server started on port 9090")
except Exception as e:
    logger.warning(f"Metrics server issue: {e}")

from flask import Flask, jsonify, render_template
from data_loader import (
    load_data,
    get_total_sales,
    get_total_volume,
    get_sales_by_productline,
    get_sales_by_country,
)

app = Flask(__name__, template_folder="templates", static_folder="static")

df = load_data()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/total-sales")
def total_sales():
    return jsonify({"total_sales": get_total_sales(df)})

@app.route("/api/total-volume")
def total_volume():
    return jsonify({"total_volume": get_total_volume(df)})

@app.route("/api/sales-by-productline")
def productline_sales():
    return jsonify(get_sales_by_productline(df))

@app.route("/api/sales-by-country")
def country_sales():
    return jsonify(get_sales_by_country(df))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
