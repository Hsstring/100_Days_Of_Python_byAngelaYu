file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
print("\n")
# 'r' -> read only
# 'w' -> write
# 'a' -> append

with open("my_file.txt", mode='a') as file:
    file.write("New text.")

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode='w') as newfile:
    newfile.write("Arrrrrrr....")
