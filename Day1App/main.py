
todos = []

while True:
    command = input("add/show/exit: ")

    match command:
        case 'add':
            todo = input("What to add? ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

