import json
import csv

counter = 0

with open('Data.json', 'r') as f:
    whitelist_dict = json.load(f)

    with open('v.csv', 'w') as csvfile:
        cwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for whitelist in whitelist_dict:
            print(whitelist['Value'])
            cwriter.writerow(whitelist['Value'])
            counter = counter + 1

print(counter)
