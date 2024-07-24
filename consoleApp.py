# from functions import get_todo, write_todo
import functions

while True:
    user_action = input("Enter add, edit, delete, show or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todos = functions.get_todo()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        functions.write_todo(todos)
    elif user_action.startswith('edit'):
        try:
            todo_number = int(user_action[5:])
            todo_number = todo_number - 1
            new_todo = input("Enter new todo: ")
            todos = functions.get_todo()
            todos[todo_number] = new_todo + "\n"
            functions.write_todo(todos)
        except ValueError:
            print("Wrong input, Please enter todo number after edit")
        except IndexError:
            print("Index value is out of range")
            continue
    elif user_action.startswith('delete'):
        try:
            num = int(user_action[7:])
            todos = functions.get_todo()
            todos.pop(num - 1)
            functions.write_todo(todos)
        except ValueError:
            print("Wrong input, Please enter todo number after delete")
        except IndexError:
            print("Index value is out of range")
            continue
    elif user_action.startswith('show'):
        todos = functions.get_todo()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1} -{item}"
            print(row)
    elif user_action.startswith('exit'):
        break
    else:
        print("Wrong Input!!")
