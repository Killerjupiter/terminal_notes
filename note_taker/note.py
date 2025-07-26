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
            print(lines[i])

def read1():
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

#to change a line in the saved text file
def over_write():
    with open("note.txt", "r") as f:
        lines = f.readlines()
        key = int(input("type line number: "))
    if key in range(len(lines)):
        lines[key] = input("type new text: ") + "\n"
        with open("note.txt", "w") as f:
            for i in range(len(lines)):
                f.write(lines[i])

#help menu and all of it's options
def help():
    print("Type 'keys' for just the keywords, 'more' for all keyword info,")
    print("or type the keyword you want more info about. Don't forget to type 'done' when done" )
    print("")
    keyword_list = list(keyword_dict.keys())
    keyword_list.remove("")
    while True:
        key = input("input examples 'keys', 'done', or '/esc': ")
        if key == "":
            break
        elif key == "keys":
            print(keyword_list)
        elif key in keyword_dict:
            print(keyword_dict[key][0])
        elif key == "more":
            key = " "
            for i in keyword_list:
                print(i)
                print(keyword_dict[i][0])
                print("")
        else:
            break
        
            
    

#so keys don't get appended into file when typing and to call functions 
keyword_dict = {
                "/esc": ["escape key exits program", escape], 
                "/read": ["read key shows all saved text read1 even numbers the lines", read, read1], 
                "/clr": ["clear key clears saved text", clear], 
                "/overwrite": ["Replaces saved text at line indicated", over_write], 
                "/help": ["shows information regarding keys", help], 
                "": ["used for programming end user need not to worry about", pass_on],
                }

#where everything comes together
print("/help is the keyword for help")
while True:
    key = input()

    if key in keyword_dict:
        keyword_dict[key][1]()

    if "1" in key and (key.replace("1", "")) in keyword_dict: #working on
        key = (key.replace("1", ""))

        try:
            if key in keyword_dict:
                keyword_dict[key][2]()
        except:
            print("not valid sub keyword")
            continue

    if key not in keyword_dict:
        write(key)
