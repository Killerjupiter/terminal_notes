#By Bealex my discord is bealex if you need me

class keywords: #not really sure how to use it but assuming I can use it for something
    pass

#moves characters written in terminal into folder
def write(key):
        with open("note.txt", "a") as f:
            f.write(key + "\n")

#hopefully save on/off
def save(key):
    global save_state #I heard global was bad but literally couldn't figure this out without
    if key == None:
        key = input("On or Off: ").capitalize()
        if key == "On":
            save_state = True
        if key == "Off":
            save_state = False
    if save_state != None:
        if save_state == True:
            write(key)
        if save_state == False:
            pass

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

#find finds the line a words written in
def find():
    key = input("find word: ")
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
                if key in lines[i]:
                    print(lines[i])

#prints all lines with line numbers that the words on
def find1():
    key = input("find word: ")
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
                if key in lines[i]:
                    print(f"{i}. {lines[i]}")

#prints only the line numbers the words on
def find2():
    print("working")
    key = input("find word: ")
    with open("note.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
                if key in lines[i]:
                    print(f"{i}. ")


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
            print(f"number of modifiers: {len(keyword_dict[key]) - 2}")
        elif key == "more":
            key = " "
            for i in keyword_list:
                print(i)
                print(keyword_dict[i][0])
                print("")
        else:
            break

#detects if a keyword has a modifier or not and acts upon it also controls save for now   
def key_modifier(key):
        if key in keyword_dict:
            if keyword_dict[key][1]() == True:
                keyword_dict[key][1]()
            elif keyword_dict[key][1]() == False:
                keyword_dict[key][1](None)   
            key = ""
        for i in key_modifier_list:
            if i in key:
                for i in range(len(key_modifier_list)):
                    num = str(i)
                    if num in key and (key.replace(num, "")) in keyword_dict:
                        key = (key.replace(num, ""))
                        try:
                            if key in keyword_dict:
                                keyword_dict[key][i + 1]()
                                key = ""
                        except:
                            print("not valid keyword modifier")
        if key != (""):
            save(key)


#so keywords don't get appended into file when typing and to call functions  
keyword_dict = {
                "/esc": ["escape key exits program /esc1 is for debug only causes save error", escape, escape],
                "/read": ["read key shows all saved text, working modifier read1", read, read1], 
                "/clr": ["clear key clears saved text", clear], 
                "/overwrite": ["Replaces saved text at line indicated", over_write], 
                "/help": ["shows information regarding keys", help,],
                "/save": ["toggles save on or off to save writing", save,],
                "/find": ["prints all lines a word appears in", find, find1, find2,],
                "": ["used for programming end user need not to worry about", pass_on],
                }

#possible sub keys still working out everything
key_modifier_list = ["1", "2", "3"]
save_state = True

#where everything comes together
print("/help is the keyword for help")
while True:
    key = input()
    key_modifier(key)