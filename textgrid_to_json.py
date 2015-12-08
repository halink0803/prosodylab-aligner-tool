import sys, os, tgt, json, csv, string

folder = sys.argv[1]

#return [read_csv(f) for f in os.listdir(directory) if f.endswith(".txt")])

#read from csv file to match
f = open("exercises.csv")
csv_f = csv.reader(f)

json_list =[]
for row in csv_f:
    json_list.append(row[1])

def match_file(f):
    for i in range(0, len(json_list)) :
        json_type = json.loads(json_list[i])
        if "audio" in json_type:
            file_name = json_type["audio"][:len(json_type["audio"])-4]
            file_name = file_name[file_name.rfind('/')+1:]
            if file_name == f:
                return i

def remove_redundant(intervals):
    count = 1
    for i in range(0, len(intervals)):
        if intervals[i].text == "REPEAT":
            index = i
    intervals = intervals[index+1:]
    intervals = [interval for interval in intervals if interval.text not in string.ascii_uppercase[:4]]

    return intervals

#handle the textgrid file
files = [file for file in os.listdir(folder) if file.endswith(".TextGrid")]
for f in files:
    tg = tgt.read_textgrid(f)
    tier = tg.get_tier_by_name('words')
    #get intervals
    intervals = [i for i in tier.intervals if i.text != 'sp' and i.text != 'sil']
    intervals = remove_redundant(intervals)

    #match the file
    index_json = match_file(f[:len(f)-9])

    #update json
    json_type = json.loads(json_list[index_json])
    count = 0
    for i in json_type["imgs"]:
        for j in i["texts"]:
            words = j["content"].split(" ")
            for index in range(0, len(words)):
                words[index] = '[' + str(intervals[count].start_time) + ']' + words[index] + '[' + str(intervals[count].end_time) + ']'
                count += 1
            j["content"] = " ".join(words)
    json_file_name = f[:len(f)-9] + ".json"
    json_file = open(json_file_name, 'w')
    json_file.write(json.dumps(json_type))
    json_file.close
    break
