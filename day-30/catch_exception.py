try:
    file = open("a_file.txt")
    a_dictionary = {"key": "Value"}
    print(a_dictionary["d"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Hello world")
except KeyError as error_message:
    print(f"That Key {error_message} doesn't exists")
else:
    content = file.read()
    print(content)
    print("Succeeded")
finally:
    file.close()
    print("File closed")