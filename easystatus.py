import time
import discord
import os
from discord.ext import commands

#insert token here
token = ""

def setDisplay():
    @client.event
    async def on_ready():
        await client.change_presence(activity = discord.Activity(type = selection, name = display))

        print ("\n[+] Server is online")
        time.sleep(1)
        print("\n[+] Connected to bot successfully: {}".format(client.user.name))
        print("\n'ctrl+c' to stop the program")

    client.run(token)

watching = discord.ActivityType.watching
listening = discord.ActivityType.listening

client = commands.Bot(command_prefix = ".")

os.system("cls")

print("\n(Enter for default)")
display = input("Input the text you'd like to display:\n")

print("\n(Enter for default)")
select = input("Watching or listening? (w or l):\n")
select = select.lower()

if select == "w":
    print("\n[+] Prefix set to 'watching'\n")
    selection = watching
    time.sleep(1)
elif select == "l":
    print("\n[+] Prefix set to 'listening'\n")
    selection = listening
    time.sleep(1)
else:
    print("\n[+] Prefix set to 'watching'\n")
    selection = watching
    time.sleep(1)

if display == "":
    #watching ...
    display = "as humanity crumbles"
    print("[+] Text set to 'as humanity crumbles'")
    setDisplay()
else:
    setDisplay()
