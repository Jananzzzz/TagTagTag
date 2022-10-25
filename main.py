import json


while True:
    instruction = input("TagTagTag: ")

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

    elif instruction == "exit()":
        break
    else: 
        print("Sorry, no such commands.")
        print("type 'help' for help or 'exit()' to exit.")




