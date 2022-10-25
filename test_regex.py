import re

txt = "the rain in spain"

dict = {
    "tag0": "0",
    "tag1": "1",
    "tag2": "2"
}

x = re.search("^the.*spain$", txt) # if no match, return None.
x = re.findall("^the.+spains$", txt)
print(x)

       
for i in dict:
    x = re.findall("^tag", i)
    if x is not None:
        for j in x: print(j)


