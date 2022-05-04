import csv
import pandas as pd

with open('/Users/anthonysung/Desktop/dict/simple_words.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
print(data[2,2])