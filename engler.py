import csv
csvReader = csv.reader(open('wordlist.csv','rb'), delimiter=' ', quotechar='|')
for row in csvReader:
    print ', '.join(row)
