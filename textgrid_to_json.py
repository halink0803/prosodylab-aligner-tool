import textgrid

with open("U2-L2-1.TextGrid", "r+") as textgrid_file:
  textgrid_file.read()

textgrid_file = textgrid.TextGrid.fromFile('U2-L2-1.TextGrid')
print textgrid_file