import sys, os, tgt


print sys.argv[1]
folder = sys.argv[1]

#return [read_csv(f) for f in os.listdir(directory) if f.endswith(".txt")])
files = [file for file in os.listdir(folder) if file.endswith(".TextGrid")]
for f in files:
    with open(f) as fi:
        tg = tgt.read_textgrid(fi)
    print tg
    break
