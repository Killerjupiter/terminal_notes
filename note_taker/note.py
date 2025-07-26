#By Bealex my discord is bealex if you need me
#moves characters written in terminal into folder
def write(key): 
    with open("note.txt", "a") as f:
        f.write(key + "\n")

#prints whatever is written in file into terminal
def read():
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            print(f"{i}. {lines[i]}")

#clears text file
def clear():
    with open("note.txt", "w") as f:
        f.write("")

#exits the program
def escape():
    exit()

#passes over so read doesn't save anything if you press enter and nothing else
def pass_on():
    pass

#to change a line in the saved text file not working
def over_write():
    with open("note.txt", "r") as f:
        lines = f.readlines()
        key = int(input("type line number: "))
    if key in range(len(lines)):
        lines[key] = input("type new text: ") + "\n"
        with open("note.txt", "w") as f:
            for i in range(len(lines)):
                f.write(lines[i])


#so keys don't get appended into file when typing and to call functions 
keyword_dict = {"/esc": escape, "/read": read, "/clr": clear, "": pass_on, "/overwrite": over_write,}

#where everything comes together
while True:
    key = input()

    if key in keyword_dict:
        keyword_dict[key]()

    if key not in keyword_dict:
        write(key)
