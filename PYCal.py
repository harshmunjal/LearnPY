x = 0
y = 0
op = ""
# Capture the user's choice
def menu_main():
    msg_welcome = "👋 Welcome to HM Cal \n \n Please input the number of the menu item from below: \n  1. Basic Calculator \n  2. Unit Converter \n  3. Exit \n" 
    sel = input(msg_welcome)
    if sel.isdigit():
        sel = int(sel)
        if sel > 0 and sel <=3 :
            print(f"your selection: {sel}")
        else :
            print("Please input a vlaid choice")
    else :
        print ("Please input a nuumber of menu item\n")
        return menu_main()
        
menu_main()

# Activate the Function related to 1the user's choice

# Basic cal function 

# Unite Convt 

# Display the result

# show main manu options after reults

# If no, exit the program


