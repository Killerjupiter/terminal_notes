#moves characters written in terminal into folder
def write(key): 
    with open("note.txt", "a") as f:
        f.write(key + "\n")

#prints whatever is written in file into terminal
def read():
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in lines:
            print(i)

#clears text file
def clear():
    with open("note.txt", "w") as f:
        f.write("")

#so keywords don't get appended into file when used
keyword_list = ["escape", "read", "clear", "",]

#where everything comes together
while True:
    key = input()

    if key == "escape":
        exit()

    if key == "read":
        read()
    
    if key == "clear":
        clear()

    if key not in keyword_list:
        write(key)