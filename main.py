from dis import Instruction
import data 

data = data.tag_data



while True:
    instruction = input("TagTagTag: ")

    if instruction == "help":
        print("help", "|", "show all the instructions")
        print("exit()", "|", "exit the program")
        print("tag -all", "|", "show all the tags and corresponding objects")

    if instruction == "tag -all":
        for i in data:
            print(i,"|", data[i] )
    

    elif instruction == "exit()":
        break
    else: 
        print("Sorry, no such commands.")
        print("type 'help' for help or 'exit()' to exit.")

# feature
# cast insensitive commands




