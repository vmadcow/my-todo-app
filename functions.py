FILEPATH = "todos.txt"

def get_todos(user_file=FILEPATH):
    """ Reads text file and return the list of
    to-do items.
    """
    with open(user_file, 'r') as file_local:
        local_todos = file_local.readlines()
    return local_todos

def write_todos(todos_arg,filepath=FILEPATH):
    """Write the to-do item in a list into a text (file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
