import json, csv, string, re
f = open("exercises.csv")
csv_f = csv.reader(f)

number = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN",  "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
tens = ["ZERO", "TEN", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]

# Convert number to string: number < 99
def number_to_string(input_number):
    str_input_number = ""
    if input_number < 20:
        str_input_number = number[input_number]
    else:
        t = input_number % 10
        if t != 0:
            str_input_number = tens[input_number / 10] + " " +number[t]
        else:
            str_input_number = tens[input_number / 10]
    return str_input_number

def standardize_string(input_string):
    s = input_string
    s = re.sub(ur"[^\w\d'\s]+",'',s)
    s = re.sub("\'.?",'', s)
    s = s.upper()
    if s.find("COLOUR") != -1:
        s = re.sub("COLOUR", "COLOR", s)
    if s.find("DOESN") != -1 :
        s = re.sub("DOESN", "DOES", s)
    if s.find("FAVOURITE") != -1:
        s = re.sub("FAVOURITE", "FAVORITE", s)
    if s.find("HAI") != -1 and s[s.find("HAI") - 1] == " ":
        s = re.sub("HAI", "HI", s)
    if s.find("HIDEANDSEEK") != -1:
        s = re.sub("HIDEANDSEEK", "HIDE AND SEEK", s)
    if s.find("ISN") != -1:
        s = re.sub("ISN", "IS", s)
    if s.find("LOC") != -1:
        s = re.sub("LOC", "LOCK", s)
    if s.find("MATHS") != -1:
        s = re.sub("MATHS", "MATH", s)
    if s.find("NOI") != -1:
        s = re.sub("NOI", "NOISE", s)
    if s.find("OLOCKK") != -1:
        s = re.sub("OLOCKK", "CLOCK", s)
    if s.find("PERTER") != -1:
        s = re.sub("PERTER", "PETER", s)
    if s.find("PHONG") != -1:
        s = re.sub("PHONG", "FONG", s)
    if s.find("SIXTYFIVE") != -1:
        s = re.sub("SIXTYFIVE", "SIXTY FIVE", s)
    if s.find("THEYE") != -1:
        s = re.sub("THEYE","THEY", s)
    if s.find("99000") != -1:
        s = re.sub("99000", "NINETY NINE THOUSAND", s)
    if s.find("HIEN") != -1:
        s = re.sub("HIEN", "HEN", s)
    if s.find("HOA") != -1:
        s = re.sub("HOA", "HA", s)
    if s.find("288COME") != -1:
        s = re.sub("288COME", "COME", s)
    if s.find("THERE259") != -1:
        s = re.sub("THERE259", "THERE", s)
    if s.find("FOOTBALLER") != -1:
        s = re.sub("FOOTBALLER", "FOOTBALL", s)
    return s

count = 1
for row in csv_f:
  if count > 80: break
  count += 1
  data = json.loads(row[1])

  #file name
  filename = ''  
  if 'audio' in data:
      filename = filename + data["audio"]
      pos = filename.rfind('/')
      filename = filename[pos+1:len(filename)-4]
  else:
      filename = str(count)
  filename = row[3] + '-' + filename + ".lab"
  file = open(filename, 'w')

  #introduction
  page_number = data["pageNumber"]
  page_number = int(page_number)
  str_page_number = number_to_string(page_number)
  lesson_number = row[5].split(" ")[1]
  unit_name = ""
  if lesson_number == "1":
      unit_name = row[4]
      unit_name = unit_name.split(" ")
      unit_name[1] = number_to_string(int(unit_name[1]))
      unit_name = " ".join(unit_name)
      unit_name = standardize_string(unit_name)
  tmp = "PAGE " + str_page_number + " " +  unit_name + " LESSON " + number[int(lesson_number)] + " ACTIVITIES ONE LOOK LISTEN AND REPEAT "
  file.write(tmp)

  #main content
  for i in range(len(data['imgs'])) :
    file.write(string.ascii_uppercase[i] + " ")
    for index in range(len(data["imgs"][i]["texts"])) :
      s = data["imgs"][i]["texts"][index]["content"]
      s = standardize_string(s)
      file.write(s + " ")
  file.close()
