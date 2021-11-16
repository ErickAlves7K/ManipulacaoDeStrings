data = []
with open("iris.data", "r") as file:
    for register in file.readlines():
        data.append(register.split(","))

print(data)