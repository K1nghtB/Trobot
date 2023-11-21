#!/bin/python3

name = input("Name, please? ")

cmd = input("Hello " + name + ", I am TroBot. What may I do for you. Enter one of my commands or type \"Help\" to get. they are case sensitive\n")

helpmenu = "\"Exe\", execute python script\n\"Quit\" Quits me\n \" Joke\", Makes me tell you a hacking related joke(Nyi)"

if cmd == "Help":

  print(helpmenu)

elif  cmd == "Exe":

  script = input("What script the script has to be located within the directory that contains me and be python, do not put the .py ending")
  try:
    with open(script + ".py", "r") as file:
        script_content = file.read()
    exec(script_content)
  except FileNotFoundError:
        print(f"Error: File \"" + script + ".py\" not found.")
  except Exception as e:
        print(f"Error executing script: " + e)
elif cmd == "Quit":
  print("Ending")
  quit()
#elif cmd == "Joke"
 
else:
 print("Error: Unknown Command\n" + helpmenu)
