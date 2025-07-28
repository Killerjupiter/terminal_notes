#By Bealex my discord is bealex if you need me

class keywords: #not really sure how to use it but assuming I can use it for something
    pass

#hopefully save on/off
def save():
    print("not implemented")
     
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

#modified read command that adds line numbers
def read1():
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            print(f"{i}. {lines[i]}")

#find working on
def find():
    key = input("find word: ")
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
                if key in lines[i]:
                    print(lines[i])

#prints all lines with line numbers
def find1():
    key = input("find word: ")
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
                if key in lines[i]:
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
            print("some keywords have modifiers like 1")
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

#detects if a keyword has a modifier and acts upon it       
def key_modifier(key):
        for i in key_modifier_list:
            if i in key:
                for i in range(len(key_modifier_list) + 1):
                    num = str(i - 1)
                    if num in key and (key.replace(num, "")) in keyword_dict:
                        key = (key.replace(num, ""))
                        try:
                            if key in keyword_dict:
                                keyword_dict[key][i]()
                        except:
                            print("not valid keyword modifier")
                            break
            elif i not in key:
                break    

#so keywords don't get appended into file when typing and to call functions 
keyword_dict = {
                "/esc": ["escape key exits program", escape], 
                "/read": ["read key shows all saved text, working modifier read1", read, read1], 
                "/clr": ["clear key clears saved text", clear], 
                "/overwrite": ["Replaces saved text at line indicated", over_write], 
                "/help": ["shows information regarding keys", help,],
                "/save": ["starts saving writing not yet implemented", save,],
                "/find": ["prints all lines a word appears in", find, find1,],
                "": ["used for programming end user need not to worry about", pass_on],
                }

#possible sub keys still working out everything
key_modifier_list = ["1", "2", "3"]

#where everything comes together
print("/help is the keyword for help")
while True:
    key = input()

    if key in keyword_dict:
        keyword_dict[key][1]()

    key_modifier(key)

    if key not in keyword_dict:
        write(key)
