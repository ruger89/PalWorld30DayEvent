import json
import os

def update_datetime(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "DateTime":
                data[key] = new_datetime
            else:
                update_datetime(value)

directory = r'your path here'

new_datetime = 638416514446850000

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)

            update_datetime(data)

            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"Updated DateTime in {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Processing complete.")