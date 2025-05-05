import sys
import csv

read_stream = csv.reader(sys.stdin)

for row in read_stream:
    query = row[0].strip()
    words = query.split()
    for word in words:
        print(f"{word.lower()},1")
