import csv

with open('YoutubeData.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
