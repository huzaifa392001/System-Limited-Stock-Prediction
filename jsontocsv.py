import json
import csv
import pandas as pd

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    # If your JSON data is a list of dictionaries, you can directly use Pandas
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)

    # If your JSON data is a dictionary with nested structures, you might need to flatten it first
    # flattened_data = flatten_json(data)  # Implement a function to flatten nested JSON if needed
    # df = pd.DataFrame(flattened_data)
    # df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    json_file_path = "./data.json"
    csv_file_path = "./output.csv"

    json_to_csv(json_file_path, csv_file_path)
