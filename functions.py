FILEPATH = "files/todos.txt"


def openfile(filepath=FILEPATH):
    """ Reads a text file and returns the list of the to-do items """
    with open(filepath, 'r') as file:
        my_list = file.readlines()
    return my_list


def writefile(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as my_file:
        my_file.writelines(todos_arg)


def displaylist(todos_local):
    for index, task in enumerate(todos_local):
        new_item = task.strip('\n')
        print(f"{index + 1}-{new_item.capitalize()}")


if __name__ == "__main__":
    print("Hello from functions")
    print(openfile())
