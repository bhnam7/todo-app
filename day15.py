# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%d/%m/%Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete and exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos('todos.txt')

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = (number - 1)

            todos = functions.get_todos()

            print("Here are the current todos: ", todos)

            new_todo = input("enter new todo item ")
            todos[number] = new_todo + '\n'
            print("here it is how it will be", todos)

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1

            todo_to_removed = todos[index].strip('\n')

            todos.pop(index)
            print("current todos: ", todos)

            functions.write_todos(todos)

            message = f"todo {todo_to_removed} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("comment is not valid")

print("bye")
