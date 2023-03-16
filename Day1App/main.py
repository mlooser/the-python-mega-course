def storetodos(todos):
    lines = [item + "\n" for item in todos]
    with open(r"data/todo.txt","w") as file:
        file.writelines(lines)


def readtodos():
    with open(r"data/todo.txt", "r") as file:
        load_items = file.readlines()
    return [item.strip("\n") for item in load_items]

todos = readtodos()

while True:
    command = input("add/show/remove/exit: ")
    command = command.strip()

    match command:
        case 'add':
            todo = input("What to add? ")
            todos.append(todo)
            storetodos(todos)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index+1}.{item}")
        case 'edit':
            index = int(input("Number of item to edit? "))
            todos[index-1]=input("New value: ")
            storetodos(todos)
        case 'remove':
            index = int(input("What to remove? "))
            todos.pop(index-1)
            storetodos(todos)
        case 'exit':
            break


