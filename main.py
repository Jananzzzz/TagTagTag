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

# function to remove/ write to json
def remove_json(tag, filename='person.json'):
    with open(filename,'r+') as file:       # r+ : read and write the file
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        for i in file_data:
            if i == tag:
                del file_data[i]
                break
        open('person.json', 'w').close()
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

while True:
    instruction = input("TagTagTag: ")

    # open read mode for later use:
    with open('person.json', 'r') as f0:
        data0 = json.load(f0)
    
    # simple tag search for objects
    if instruction in data0:
        print(data0[instruction])
        continue

    elif instruction == "help":
        print("help", "|", "show all the instructions")
        print("exit()", "|", "exit the program")
        print("all", "|", "show all the tags and corresponding objects")
        print("tag -all", "|", "show all objects with in the same tag prefix")
        print("# tag", "|", "add a tag behind #")
        print("remove # tag", "|", "remove the tag behind #")


    # show all objects
    elif instruction == "all":
        with open('person.json', 'r') as f:
            data = json.load(f)
            for i in data:
                print(i, "|", data[i])

    # show all results with prefix tag
    elif re.search("-all$", instruction):
        tag = instruction[:-5]
        count = 0
        for i in data0:
            if re.search(f"^{tag}.*", i):
                print(i, "|", data0[i])
                count += 1
        if count == 0:
            print("there is no such tag :(")
    
    # show the objects under the tag.
    elif instruction in data0:
        print(data0[instruction])

    # remove a tag 
    elif re.search('^remove', instruction):
        tag = instruction[9:]
        remove_json(tag)
        

    # add a tag
    elif re.search('#\s.+', instruction):
        tag = instruction[2:]
        if tag in data0:
            print("This tag is already exist, you can add a suffix to your tag :)")
            ans = input(f"want to see all tags with a prefix '{tag}'? (y/n):")
            if ans == 'n': continue
            else:
                for i in data0:
                    if re.search(f"^{tag}.*", i):
                        print(i, "|", data0[i])
                continue
        content = input(f"input your content for tag '{tag}': ")
        write_json(tag, content)


    elif instruction == "exit()":
        break
    else: 
        print("Sorry, no such commands or tags :(")
        print("type 'help' for help or 'exit()' to exit.")




