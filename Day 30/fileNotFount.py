# FileNotFound with try and except

try:
    file = open("a_file.txt")
    dic = {"key": "value"}
    print(dic["smtng"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("SOMETHIIIING")
except KeyError as error_message:
    print(f"That key {error_message}does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")


