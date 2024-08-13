1. Install the necessary packages:

```bash
pip install -r requirements.txt
pip install --upgrade Flask Werkzeug
```

2. Run the Flask application:

```bash
python app.py
```

```bash
py app.py
```


 Hit below endpoints:
3. Fetching and processing data:

GET http://127.0.0.1:5000/fetch-data

4. Retrieving processed data:

GET http://127.0.0.1:5000/get-processed-data


Explanation

/fetch-data: This endpoint simulates fetching data from an external service and processes it by transforming customer names to uppercase. The processed data is stored in a global dictionary (processed_data_store).
process_data: This function is responsible for processing the fetched data. In this example, it converts all customer names to uppercase.
/get-processed-data: This endpoint retrieves the processed data from the in-memory store and returns it as a JSON response. If no data is available, it returns a 404 response.













