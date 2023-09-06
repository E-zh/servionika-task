import argparse
import json
import os

# Get path to storage data file
storage_path = os.path.realpath('storage.data')

# Create file if not exists
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        json.dump({}, f)


# Get data from storage file by key
def get_value(key):
    with open(storage_path, 'r') as f:
        data = json.load(f)
        return data.get(key, None)


# Get all data from storage file
def get_all_values():
    with open(storage_path, 'r') as f:
        return json.load(f)


# Set data to storage file
def set_value(key, value):
    with open(storage_path, 'r') as f:
        data = json.load(f)
    data[key] = value
    with open(storage_path, 'w') as f:
        json.dump(data, f)


# Handling Command Line Arguments
parser = argparse.ArgumentParser(description='Utility for working with key-values storage')
parser.add_argument('--key', type=str, help='Key for save/get value')
parser.add_argument('--val', type=str, help='Value for save')
parser.add_argument('--all', action='store_true', help='Get all data from storage file')

args = parser.parse_args()

if args.all:
    all_data = get_all_values()
    for key, value in all_data.items():
        print(f'{key}: {value}')
elif args.key:
    if args.val:
        set_value(args.key, args.val)
        print('Value saved successfully.')
    else:
        result = get_value(args.key)
        if result is not None:
            print(f'Key value {args.key}: {result}')
        else:
            print('Value not found.')
else:
    print('Key required --key to access data or key --all to get all data.')
