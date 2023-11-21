#!/bin/python3

name = input("Name, please? \n")

cmd = input("Hello " + name + ", I am TroBot. What may I do for you. Enter one of my commands or type \"Help\" to get. they are case sensitive\n")

helpmenu = "\"Exe\", execute python script\n\"Quit\" Quits me\n \" Joke\", Makes me tell you a hacking related joke"

if cmd == "Help":

  print(helpmenu)

elif  cmd == "Exe":

  script = input("What script the script has to be located within the directory that contains me and be python, do not put the .py endingn\n")
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
elif cmd == "Joke":
 
  Jokelist = ["What is a hacker's favorite season, phishing season","What do you call a turtle that surfs the dark web, a TORtoise","What do you call an excavated pyramid? Unencypted","What's the best way to catch a runaway robot? Use a botnet","What do you tell a hacker after a breakup? There are plenty of phish in the sea","What did the hacker's out of office message say? Gone phishing!","Why was the hacker's californian hiking trip interrupted? There was a firewall"]
  import random
  joke = random.choice(Jokelist)
  print(joke)
else:
 print("Error: Unknown Command\n" + helpmenu)
