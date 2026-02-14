# -------------------------------------------------
# File Name: 02_access_by_key.py
# Author: Florentino Báez
# Date: Variables - Dictionaries
# Description: Access Dictionary Values by Key.
#              Shows how to retrieve values using bracket
#              notation dict[key]. Raises KeyError if the
#              key does not exist in the dictionary.
# -------------------------------------------------

# Example 2: Access dictionary values by key
print("Example 2: Access dictionary values by key")
print("-" * 40)

# Dictionary with personal information
person = {"name": "Maria Lopez", "age": 25,
          "city": "New York", "profession": "Engineer","major": "Computer Science","address": "123 Main St, Anytown, USA","email": "maria.lopez@example.com","phone": "1234567890"}

print("Person Information:", person)
print("Name:", person["name"])          # Access value using key
print("Age:", person["age"])            # Returns the value mapped to "age"
print("City:", person["city"])          
print("Major:", person["major"])        
print("Address:", person["address"])    
print("Email:", person["email"])        
print("Phone:", person["phone"])        

#add sex
person["sex"] = "Female"
print("Sex:", person["sex"])        

#add gpa
person["gpa"] = 3.8
print("GPA:", person["gpa"])        

#add skills
person["skills"] = ["Python", "JavaScript", "SQL"]
print("Skills:", person["skills"])        

#add ssn
person["ssn"] = "123-45-6789"
print("SSN:", person["ssn"])        

#add birthdate
person["birthdate"] = "1990-01-01"
print("Birthdate:", person["birthdate"])       

#add height
person["height"] = 1.75
print("Height:", person["height"])       

#add weight
person["weight"] = 70
print("Weight:", person["weight"])   

#edit age
person["age"] = 26
print("Age:", person["age"])   

# loop through the dictionary and print the only the keys
print("Loop through the dictionary and print the key")
for key in person.keys():
    print(f"{key}")

# loop through the dictionary and print the only the values
print("Loop through the dictionary and print the only the values")
for value in person.values():
    print(f"{value}")

# loop through the dictionary and print the only the values
print("Loop through the dictionary and print the key and value")
for key, value in person.items():
    print(f"{key}: {value}")

# Loop through the dictionary and print the key and value
print("Loop through the dictionary and print the key and value")
for key, value in person.items():
    print(f"{key}: {value}")

'''
rules for keys:
- keys must be immutable
- keys must be unique
- keys must be hashable
- values keys must be: string, number, boolean, tuple, list, dictionary, set
'''