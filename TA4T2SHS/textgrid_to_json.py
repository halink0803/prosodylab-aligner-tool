import sys, os, tgt, json, csv, string, MySQLdb

folder = sys.argv[1]

#return [read_csv(f) for f in os.listdir(directory) if f.endswith(".txt")])

#read from csv file to match
csv_file = [file for file in os.listdir(folder) if file.endswith(".csv")]
f = open(csv_file[0])
csv_f = csv.reader(f)

json_list =[]
id_list = []
for row in csv_f:
    json_list.append(row[1])
    id_list.append(int(row[0]))

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
    for i in string.ascii_uppercase[:4]:
        for j in intervals:
            if i == j.text:
                intervals.remove(j)
                break
    # intervals = [interval for interval in intervals if interval.text not in string.ascii_uppercase[:4]]

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
    print f
    for i in json_type["imgs"]:
        for j in i["texts"]:
            words = j["content"].split(" ")
            j["begin"] = str(intervals[count].start_time)
            # print words
            for index in range(0, len(words)):
                print words[index]
                print intervals[count]
                words[index] = '[' + str(intervals[count].start_time) + ']' + words[index] + '[' + str(intervals[count].end_time) + ']'
                count += 1
                if count == len(words)-1:
                    j["end"] = str(intervals[count].end_time)
            j["content"] = " ".join(words)
    # json_file_name = f[:len(f)-9] + ".json"
    # json_file = open(json_file_name, 'w')
    # json_file.write(json.dumps(json_type))
    # json_file.close

    #update sql
    db = MySQLdb.connect("localhost", "root", "t00r", "sachmem_development", unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock")

    cursor = db.cursor()

    # cursor.execute("SELECT VERSION()")

    sql = "UPDATE exercises SET content = %s WHERE id = %s"

    # Execute the SQL command
    cursor.execute(sql, (json.dumps(json_type), id_list[index_json] ))
    # Commit your changes in the database
    db.commit()
    db.close
