import sys, os, tgt, json, csv

folder = sys.argv[1]

#return [read_csv(f) for f in os.listdir(directory) if f.endswith(".txt")])

#handle the textgrid file
files = [file for file in os.listdir(folder) if file.endswith(".TextGrid")]
for f in files:
    tg = tgt.read_textgrid(f)
    tier = tg.get_tier_by_name('words')
    intervals = [i for i in tier.intervals if i.text != 'sp']
    for interval in intervals:
        print interval
    break

#read from csv file to match
f = open("exercises.csv")
csv_f = csv.reader(f)

for row in csv_f:
    print row
    break
