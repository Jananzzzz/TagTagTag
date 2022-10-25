import re

txt = "the rain in spain"

x = re.search("^the.*spain$", txt) # if no match, return None.
x = re.findall("^the.+spain$", txt)
for i in x:
    print(i)



