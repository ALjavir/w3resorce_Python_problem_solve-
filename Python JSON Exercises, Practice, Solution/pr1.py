#1. Write a Python program to convert JSON data to Python object.
import json
j_obj = '{"name" : "Tonmoy", "Hobby" : "scrow you", "age":"go to hell" }'
p_obj = json.loads(j_obj)
print("Name: ",p_obj["name"])
print("Hobby: ",p_obj["Hobby"])
print("age: ",p_obj["age"])