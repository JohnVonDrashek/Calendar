import sys

commands = ["list", "exit", "add", "read", "delete"]

complete = False
while(not complete):
    u_in = input("Type a command (type 'list' if you don't know)\n")

    if u_in == commands[0]:
        print(commands)
    elif u_in == commands[1]:
        complete = True
    elif u_in == commands[2]:
        calendar = open("calendar.dat","a+")
        entry = input("add event name, date, and time in the format: EVENTNAME MM-DD-YYYY HH:MM\n")
        calendar.write(entry + "\n")
        calendar.close()
    elif u_in == commands[3]:
        calendar = open("calendar.dat","r+")
        print(calendar.read())
        calendar.close()
    elif u_in == commands[4]:
        calendar = open("calendar.dat","r")
        for index, line in enumerate(calendar):
            print(str(index) + ": " + line)
        line_to_delete = input("enter number of line to delete\n")
        calendar.close()
        calendar = open("calendar.dat","r+")
        lines = calendar.readlines()
        calendar.close()
        calendar = open("calendar.dat","w")
        calendar.truncate(0)
        counter = 0
        for line in lines:
            if counter != line_to_delete:
                calendar.write(line)
            counter += 1
        calendar.close()
        
calendar.close()
