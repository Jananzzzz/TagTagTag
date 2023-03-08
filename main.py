import json
import re
from fuzzywuzzy import fuzz

# function to add to JSON
def write_json(tag, content, filename):
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
def remove_json(tag, filename):
    with open(filename,'r+') as file:       # r+ : read and write the file
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        for i in file_data:
            if i == tag:
                del file_data[i]
                break
        open(filename, 'w').close()
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

while True:
    instruction = input("TagTagTag: ")

    # open read mode for later use:
    with open('data.json', 'r') as f0:
        data0 = json.load(f0)
    with open('task.json', 'r') as f1:
        data1 = json.load(f1)
    with open('password.json', 'r') as f2:
        data2 = json.load(f2)
    
    # simple tag search for objects
    if instruction in data0:
        print(instruction, "|", data0[instruction])
        continue

    elif instruction == "help":
        print("help", "|", "show all the instructions")
        print("exit()", "|", "exit the program")
        print("all", "|", "show all the results with a fuzzy search")
        print("<your tag>", "|", "show the corresponding content")
        print(".<your tag>", "|", "show the most related results to <your tag>")
        print("<your tag> -all", "|", "show all objects related to <your tag>")
        print("# tag", "|", "add a tag behind #")
        print("remove # <your tag>", "|", "remove the tag behind #")
        print("task", "|", "show all the tasks")
        print("addtask", "|", "add a task")
        print("rmtask k", "|", "remove the kth task")
        print("pwd", "|", "show all password")
        print("addpwd <your password tag>", "|", "add a password")
        print("rmpwd tag", "|", "remove a password")
        print("pwd <your password tag>", "|", "show the password of the tag")
        print("pwd <your password tag> -all", "|", "show all the related password")
        
        
        


    # show all objects
    elif instruction == "all":
        print('')
        for i in data0:
            print(i, "|", data0[i], "\n")

    # find the most suittable results
    elif re.search("^\.", instruction):
        tag = instruction[1:]
        number = ''
        result = ''
        max = 0
        for i in data0:
            ratio = fuzz.partial_ratio(i, tag)
            if ratio > max:
                max = ratio
                number = i
                result = data0[i]
            if ratio == max:
                if len(number) < len(i):
                    continue
                else:
                    max = ratio
                    number = i
                    result = data0[i]
        if max > 40:
            print(number, "|", result)
        else:
            print("there seems no related result :(")

        
                

    # show all results with a fuzzy search 
    elif re.search("-all$", instruction) and not re.search("^pwd.+-all$", instruction):
        tag = instruction[:-5]
        count = 0
        for i in data0:
            ratio = fuzz.partial_ratio(i, tag)
            if ratio >= 70: 
            # if re.search(f"^{tag}.*", i):
                print(i, "|", data0[i], "\n")
                count += 1
        if count == 0:
            print("there is no such tag :(")

    # show all passwords with a fuzzy search
    elif re.search("^pwd\s.+-all$", instruction):
        tag = instruction[4:-6]
        count = 0
        for i in data2:
            ratio = fuzz.partial_ratio(i, tag)
            if ratio >= 70:
                print('')
                print(i)
                print(data2[i])
                count += 1
        if count == 0:
            print("there is no such password :(")
        else:
            print("")

    
    # show the objects under the tag.
    elif instruction in data0:
        print(data0[instruction])

    elif re.search('^pwd\s', instruction):
        tag = instruction[4:]
        if tag in data2:
            print("")
            print(data2[tag])
            continue
        print("sorry, no such password :(")

    # remove a tag 
    elif re.search('^remove', instruction):
        tag = instruction[9:]
        if tag in data0:
            remove_json(tag, 'data.json')
        else:
            print("Sorry, there is no such tag :(")
            continue
    
    # show all the tasks
    elif instruction == "task":
        count = 0
        for i in data1:
            print(i, "|", data1[i])
            count += 1
        if count == 0:
            print("you are updated! :)")

    # show all the passwords
    elif instruction == "pwd":
        for i in data2:
            print("")
            print(i)
            print(data2[i])
        print("")

    elif re.search('^rmtask', instruction):
        number = instruction[7:]
        if number in data1:
            remove_json(number, 'task.json')
        else:
            print("Sorry, there is no such number :(")
            continue

    elif re.search('^rmpwd', instruction):
        tag = instruction[6:]
        if tag in data2:
            remove_json(tag, 'password.json')
        else:
            print("sorry, there is no such password :(")

    elif instruction == "addtask":
        dict_key = data1.keys()
        key_list = list(dict_key)
        if len(key_list) == 0:
            last_number = 0
        else:
            last_number = int(key_list[-1])
        number = last_number + 1
        print("input your task:")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        space = " " * len(str(number))
        content = f'\n{space} | '.join(lines)
        write_json(str(number), content, 'task.json')

        
    # add a password "addpwd <your password tag>"
    elif re.search('^addpwd\s.+', instruction):
        tag = instruction[7:]
        if tag in data2:
            print("This tag already exists, you can add a suffix to your tag :)")
            ans = input(f"want to see all tags with a prefix '{tag}'? (y/n):")
            if ans == 'n': continue
            else:
                for i in data2:
                    if re.search(f"^{tag}.*", i):
                        print(i, "|", data2[i])
                continue
        lines = [""] * 5 
        lines[0] = "Username: " + input("Username: ")
        lines[1] = "Password: " + input("Password: ")
        lines[2] = "Email   : " + input("Email: ")
        lines[3] = "Phone   : " + input("Phone: ")
        lines[4] = "Others  : " + input("Others: ")
        content = '\n'.join(lines)
        write_json(tag, content, 'password.json')
        


    # add a tag
    elif re.search('#\s.+', instruction):
        tag = instruction[2:]
        if tag in data0:
            print("This tag already exists, you can add a suffix to your tag :)")
            ans = input(f"want to see all tags with a prefix '{tag}'? (y/n):")
            if ans == 'n': continue
            else:
                for i in data0:
                    if re.search(f"^{tag}.*", i):
                        print(i, "|", data0[i])
                continue
        lines = []
        print("input your content:")
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        space = " " * len(tag)
        content = f'\n{space} | '.join(lines)
        write_json(tag, content, 'data.json')


    elif instruction == "exit()":
        break
    else: 
        print("Sorry, no such commands or tags :(")
        print("type 'help' for help or 'exit()' to exit.")




