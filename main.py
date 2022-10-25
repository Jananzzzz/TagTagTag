import json
import re


# function to add to JSON
def write_json(tag, content, filename='person.json'):
    with open(filename,'r+') as file:       # r+ : read and write the file
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[tag] = content
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

while True:
    instruction = input("TagTagTag: ")

    with open('person.json', 'r') as f0:
        data0 = json.load(f0)

    with open('person.json', 'r') as f:
        data = json.load(f)
        if instruction in data:
            print(data[instruction])
            continue

    if instruction == "help":
        print("help", "|", "show all the instructions")
        print("exit()", "|", "exit the program")
        print("tag -all", "|", "show all the tags and corresponding objects")

    elif instruction == "tag -all":
        with open('person.json', 'r') as f:
            data = json.load(f)
            for i in data:
                print(i, "|", data[i])
    
    # show the objects under the tag.
    elif instruction in data0:
        print(data0[instruction])

    elif re.search('#\s.+', instruction):
        tag = instruction[2:]
        content = input(f"input your content for tag '{tag}': ")
        write_json(tag, content)


    elif instruction == "exit()":
        break
    else: 
        print("Sorry, no such commands.")
        print("type 'help' for help or 'exit()' to exit.")




