from flask import Flask, jsonify
import random
# from urllib.parse import quote

app = Flask(__name__)

processed_data_store = {}

# nested dictionary for mock data
mock_data = {
    "orders": [
        {"order_id": 1, "total_amount": 300, "customer": "Salman"},
        {"order_id": 2, "total_amount": 500, "customer": "Catalys"},
        {"order_id": 3, "total_amount": 1000, "customer": "Shalrique"},
    ]
}

# for fetching data endpoint
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Retrieval from an external source
    fetched_data = mock_data
    # Process the data
    # calling process data function
    process_data(fetched_data)
    return jsonify({"message": "Data fetched and processed successfully"}), 200

# fetched data processing function
def process_data(data):
    global processed_data_store
    # Only Convert customer names to uppercase
    processed_orders = []
    for order in data['orders']:
        processed_order = {
            "order_id": order['order_id'],
            "total_amount": order['total_amount'],
            "customer": order['customer'].upper()
        }
        processed_orders.append(processed_order)
    # storing processed data in memory
    processed_data_store['orders'] = processed_orders

# processed data endpoint
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if not processed_data_store:
        return jsonify({"message": "No data available"}), 404
    return jsonify(processed_data_store), 200

if __name__ == '__main__':
    app.run(debug=True)
