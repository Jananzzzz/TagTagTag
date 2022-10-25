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
 
     
write_json("testwirte", "1234")

# json.loads() parse json object into python dict
# json.dumps() convert python object into json string


