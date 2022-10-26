from cgi import test
from msvcrt import LK_LOCK, kbhit


dict = {}
dict["tag0"] = '''this is a tag.
this is also tag in a different line.'''
lines = []
while True:
  line = input()
  if line:
    lines.append(line)
  else:
    break
text = '\n'.join(lines)
print(text)

dict["tag1"] = text
for i in dict:
  print(i, "|", dict[i])

print(dict)