import csv
import sys
import datetime

def getDate (text):
    return datetime.datetime.strptime(text, "%Y%m%d")

filePath = sys.argv[1]
with open(filePath, newline='') as csvfile:
    bankreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in bankreader:
        print(getDate(row['Data transakcji']))
