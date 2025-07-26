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

def escape():
    exit()

#so keys don't get appended into file when typing and to call functions 
keyword_dict = {"escape": escape, "read": read, "clear": clear,}

#where everything comes together
while True:
    key = input()

    if key in keyword_dict:
        keyword_dict[key]()

    if key not in keyword_dict:
        write(key)
