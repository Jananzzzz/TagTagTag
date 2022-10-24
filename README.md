# TagTagTag 
## Intro <br>
**TagTagTag** is  a **Knowledge manage System**, which I want to create to facilitates my study and life. The system must have these properties: 
- Simple and easy to UI and operation 
- Storage and Query
- Efficient and Robust

To be simple, the form of the system is based on **terminal**. 

## Basic commands
**Return objects with Tag "yourtag":**
```
$ tag "your tag"
```
*This command will return all the objects with the tag "yourtag".*

**Add a Tag:**
```
$ addtag "yourtag" "your object"
```
 *This command will add a tag with your object.*

**Remove a Tag:**
```
$ removetag "yourtag" "your object"
```
*This command will remove the tag of the object (Or say it removes the item under this tag).*
*Though it is a little bit difficult to type the object of a tag(the object may as long as a paragraph), you can first use the 'tag' command to retrieve the object of a tag.*

**Show all the tags under the same object:**
```
$ showtag "your object"
```

## Advanced commands
> Commands here will not necessarily implemented for the sake of keeping simple or just techinal problem.

**Modify object:**
```
$ mod tag "your object number"
```
*'Cause a tag can correspond to multiple objects, the objects will be numbered by FIFO principle.*

## Some hints
- A tag can correspond to more than one object
- An object will be deleted if and only if all of its tags have been removed