import csv

def save_data(data):
    with open('storage.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writerow(data)


def get_data():

    return True