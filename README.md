# TagTagTag 
## Intro <br>
**TagTagTag** is  a **Knowledge manage System**, which is created to facilitates my study and life. The system has these properties: 
- Simple and easy to UI and operation 
- Storage and Query
- Efficient and Robust

To be simple, the form of the system is based on **terminal**. 

## Basic commands
**Show all the commands for help:**
```
$ help
```
**Exit the program:**
```
$ exit()
```
**Return objects with Tag "yourtag":**
```
$ "your tag"
```
Add a `-all` to show all the objects with the prefix "your tag":
```
$ "your tag" -all
```
*This command will return all the objects with the tag "yourtag".*

**Add a Tag:**
```
$ # "your tag"
```
 *This command will add open an input line for your to input the correspoonding objects.*

**Remove a Tag:**
```
$ remove # "your tag"
```
*This command will remove the tag and the object.*

**Daily Task Part:**
```
$ task      # show all the tasks you add.
$ addtask   # add a task
$ rmtask 4  # remove the task with a sequence number of 4
```


## Advanced Commands
> Commands here will not necessarily implemented for the sake of keeping simple or just techinal problem.

**Modify object:**
```
$ mod tag "your object number"
```
*'Cause a tag can correspond to multiple objects, the objects will be numbered by FIFO principle.*

## Some hints
- A tag can correspond to more than one object
- An object will be deleted if and only if all of its tags have been removed

## More features
- autocompletion 
