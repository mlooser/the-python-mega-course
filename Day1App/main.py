
todos = []

while True:
    command = input("add/show/exit: ")
    command = command.strip()

    match command:
        case 'add':
            todo = input("What to add? ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(index, "-", item)
        case 'edit':
            index = int(input("Number of item to edit? "))
            todos[index]=input("New value: ")
        case 'exit':
            break

