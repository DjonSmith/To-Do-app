import os
import time


tasklist = []

class Task:
    def __init__(self, description, status="undone"):
        self.description = description
        self.status = status


def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass


def add_task():
    desc = input("Enter task: ")
    tasklist.append(Task(desc))


def del_task():
    try:
        user_del_input = int(input("Which task should I delete? ")) - 1
        if 0 <= user_del_input < len(tasklist):
            tasklist.pop(user_del_input)
        else:
            raise ValueError
    except ValueError:
        print("Invalid input!")
        time.sleep(2)


def mark_task():
    try:
        user_input = int(input("Which task should I mark? ")) - 1
        if 0 <= user_input < len(tasklist):
            tasklist[user_input].status = "done" if tasklist[user_input].status == "undone" else "undone"
        else:
            raise ValueError
    except ValueError:
        print("Invalid input!")
        time.sleep(2)


def edit_task():
    try:
        edit_input = int(input("Which task should I edit? ")) - 1
        if 0 <= edit_input < len(tasklist):
            print(f"Current task: {tasklist[edit_input].description}")
            tasklist[edit_input].description = input("Enter an updated task: ")
        else:
            raise ValueError
    except ValueError:
        print("Invalid input!")
        time.sleep(2)


def change_order():
    try:
        what_to_move = int(input("Which task should I move? ")) - 1
        where_to_move = int(input("Where should I move the task? ")) - 1
        if 0 <= what_to_move < len(tasklist) and 0 <= where_to_move < len(tasklist):
            tasklist.insert(where_to_move, tasklist.pop(what_to_move))
        else:
            raise ValueError
    except ValueError:
        print("Invalid input!")
        time.sleep(2)


def main():
    while True:
        clear_screen()
        print("Task List:")
        for index, task in enumerate(tasklist, start=1):
            status_symbol = '\u0336' + '\u0336'.join(task.description) if task.status == "done" else task.description
            print(f"{index} | {status_symbol}")
        
        print("\na - add new task\n" 
              "m - mark done/undone\n"
              "d - delete task\n" 
              "e - edit task\n" 
              "c - change task position\n" 
              "q - exit\n")
        user_input = input()
        match user_input:
            case "a":
                add_task()
            case "d":
                del_task()
            case "m":
                mark_task()
            case "e":
                edit_task()
            case "c":
                change_order()
            case "q":
                print("Goodbye!")
                time.sleep(2)
                clear_screen()
                break
            case _:
                print("Invalid input")
                time.sleep(2)

if __name__ == "__main__":
    main()