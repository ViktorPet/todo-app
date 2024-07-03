FILEPATH = './todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text files
        to - do list items

    """
    # with open('/home/viktor/dev_projects_10/python/experiments/todos.txt','r') as file_local:
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
