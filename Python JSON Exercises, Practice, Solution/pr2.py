#2. Write a Python program to convert Python object to JSON data.
import json
j_obj = {
    "name": "Tonmoy",
    "hobby": "Fuck you",
    "age": "go to hell"
}
a = json.dumps(j_obj)
print(a, end=" ")