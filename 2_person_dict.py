person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)
# name of the second child
print(type(person.get["children"]))
print(person["children"][1])

# name of the cat
print(type(person["pets"]))
print(person["pets"]["cats"])

# use a for loop to list each child
for i in person["children"]:
    print(i)

# print out the pets in this format;
# 'Type of pet: dog
for i, j in person["pets"].items():
    print(f"Type of pet: {i} name of pet: {j}")
