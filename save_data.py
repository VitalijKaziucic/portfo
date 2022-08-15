import csv
from operator import ne


def write_data(filename, data):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(data)
