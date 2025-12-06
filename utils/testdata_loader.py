import json
import os

def load_test_data(file_name):
    base_path = os.path.join((os.getcwd()),file_name)
    file_path = os.path.join(base_path,file_name)

    with open(file_path) as f:
        data = json.load(f)
        return data