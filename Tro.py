#!/bin/python3

name = input("Name, please? ")

cmd = input("Hello " + name + ", I am TroBot. What may I do for you. Enter one of my commands or type \"Help\" to get. they are case sensitive\n")

helpmenu = "\"Exe\", execute python script\n\"Quit\" Quits me"

if cmd == "Help":

  print(helpmenu)

elif  cmd == "Exe":

  script = input("What script the script has to be located within the directory that contains me and be python, do not put the .py ending")
  run(script)

elif cmd == "Quit":
  print(Ending)
  quit()
else:
  print("ERROR: INVALID COMMAND\n" + helpmenu)
  
