#4. Write a Python program to convert Python dictionary object (sort by key) to JSON data.
#Print the object members with indent level 4.
import json
a = "{'1':9,'2':8,'3':7,'4':6}"
print("\n","Jason data: ")
b = (json.dumps(a, sort_keys= True, indent=4))
print(b)