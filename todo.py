#  Our To-Do tool from scratch
# # Essential functions
# - [x] Add task
# - [x] Delete task
# - [x] Mark task as done/undone
# - [x] Edit task
# - [x] Change task order
# # Advanced functions
# - [ ] Create tasklist file
# - [ ] Open tasklist file
# - [ ] Delete tasklist file
# - [ ] Change tasklist file


import os
import time


tasklist = []
complist = []


def clear_screen():
    os.system('cls' if os.name == 'nt'else 'clear')


def add_task():
    tasklist.append(input("Enter task: "))
    complist.append("undone")


def del_task():
    user_del_input = int(input("Which task I should delete? "))-1
    if 0 <= user_del_input < len(tasklist):
        tasklist.pop(user_del_input)
        complist.pop(user_del_input)
    else:
        print("Invalid input!")
        time.sleep(2)


def mark_task():
    user_input = int(input("Which task should I mark? "))-1
    if 0 <= user_input < len(complist):
        if complist[user_input] == "done":
            complist[user_input] = "undone"
        elif complist[user_input] == "undone":
            complist[user_input] = "done"
    else:
            print("Invalid input!")
            time.sleep(2)


def edit_task():
    edit_input = int(input("Which task should I edit? "))-1
    if 0 <= edit_input < len(tasklist):
        print(tasklist[edit_input])
        tasklist[edit_input] = str(input("Enter an updated task: "))
    else:
        print("Invalid input!")
        time.sleep(2)

def change_order():
    what_to_move = int(input("Which task should I move? "))-1
    where_to_move = int(input("Where should I move the task? "))-1
    if 0 <= what_to_move < len(tasklist) and 0 <= where_to_move < len(tasklist):
        element = tasklist.pop(what_to_move)
        new_position = where_to_move
        tasklist.insert(new_position, element)
    else:
        print("Invalid input!")
        time.sleep(2)


def main():
    while True:
        clear_screen()
        print("Task List:")
        for x in tasklist:
            list_index = int(tasklist.index(x))+1
            if complist[list_index-1] == "undone":
                print((list_index), x, sep=" | ")
            else:
                print(str(list_index), '\u0336'+'\u0336'.join(x), sep=" | ") 
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
                exit()
            case _:
                print("Invalid input")
                time.sleep(2)


main()
