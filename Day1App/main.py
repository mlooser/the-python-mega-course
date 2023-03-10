
todos = []

while True:
    command = input("add/show/exit: ")
    command = command.strip()

    match command:
        case 'add':
            todo = input("What to add? ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

