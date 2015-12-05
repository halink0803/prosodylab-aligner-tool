# import json, csv, string, re
# # with open('exercises.json') as data_file:
#   # data  = json.load(data_file)
# # print data[0]["content"][0]
# f = open("exercises.csv")
# csv_f = csv.reader(f)
# # tmp = "ONE LOOK LISTEN AND REPEAT"
# remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
# count = 1;
# for row in csv_f:
#   # print row[1]
#   data = json.loads(row[1])
#   arr = row[4].split(" ")
#   ar = row[5].split(" ")
#   a = row[6].split(" ")
#   filename = arr[0][0] + arr[1] + '-' + ar[0][0] + ar[1] + '-' + a[0][0];
#   # print data
#   filename = filename + ".lab"
#   file = open(filename, 'w')
#   for i in range(len(data["imgs"])) :
#       file.write(string.ascii_uppercase[i] + " ")
#     for index in range(len(data["imgs"][i]["texts"])) :
#       s = data["imgs"][i]["texts"][index]["content"]
#       # s = s.translate(remove_punctuation_map)
#       s = re.sub(ur"[^\w\d'\s]+",'',s)
#       file.write(s.upper() + " ")
#   file.close()
import json, csv, string, re
f = open("exercises.csv")
csv_f = csv.reader(f)

number = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN",  "SEVENTEEN", "EIGHTEEN", "NINETEEN"]
tens = ["ZERO", "TEN", "TWENTY", "THIRTY", "FOURTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY"]

count = 1
for row in csv_f:
  if count > 80: break
  count += 1
  data = json.loads(row[1])

  #file name
  if 'audio' in data:
      filename = data["audio"]
      pos = filename.rfind('/')
      filename = filename[pos+1:len(filename)-4]
  else:
      filename = str(count)
  filename = filename + ".lab"
  file = open(filename, 'w')

  #introduction
  page_number = data["pageNumber"]
  page_number = int(page_number)
  if page_number < 20:
      str_page_number = number[page_number]
  else:
      t = page_number % 10
      if t != 0:
          str_page_number = tens[page_number / 10] + " " +number[t]
      else:
          str_page_number = tens[page_number / 10]
  lesson_number = row[5].split(" ")[1]
  tmp = "PAGE " + str_page_number + " LESSON " + number[int(lesson_number)] + " ACTIVITIES ONE LOOK LISTEN AND REPEAT "
  file.write(tmp)

  #main content
  for i in range(len(data['imgs'])) :
    file.write(string.ascii_uppercase[i] + " ")
    for index in range(len(data["imgs"][i]["texts"])) :
      s = data["imgs"][i]["texts"][index]["content"]
      s = re.sub(ur"[^\w\d'\s]+",'',s)
      file.write(s.upper() + " ")
  file.close()
