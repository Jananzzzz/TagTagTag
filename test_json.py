import json

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
def remove_json(tag, filename='test.json'):
    with open(filename,'r+') as file:       # r+ : read and write the file
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        for i in file_data:
            if i == tag:
                del file_data[i]
                break
        print(file_data)
        open('test.json', 'w').close()
        # Sets file's current position at offset.
        file.seek(0)

        # convert back to json.
        json.dump(file_data, file, indent = 4)

#write_json("make2", "1234")
remove_json('tag0')


# json.loads() parse json object into python dict
# json.dumps() convert python object into json string
