# I AM AWARE THIS IS NOT AN OS. IT'S SIMPLY A PROJECT THAT IS OS-LIKE
# Feel free to improve this or test it for yourself.
# IT IS IN VERY EARLY DEVELOPMENT. I WILL BE ADDING MORE AND UPDATING THE GITHUB REPO.
# Expect updates a few times a month
# Credits: LinuxUser59 on GitHub (me)
# Each function will have basic (~5-10 word) explanation above

######################################################################################

# Importing required packages

import webbrowser
import threading
import os
import subprocess
import socket
import platform
import shutil
import readline
import atexit


# Adding functionality for command history

histfile = os.path.expanduser("~/.OriOS_history")
try:
    readline.read_history_file(histfile)
except FileNotFoundError:
    pass
atexit.register(readline.write_history_file, histfile)


# Simple fastfetch using os, socket, platform

def fastfetch():
    username = os.getlogin()
    hostname = socket.gethostname()
    python_ver = platform.python_version()
    system = "ORION/ORI OS"
    release = "2026-03-25-OrionOS"
    home = os.path.expanduser("~")
    shell = os.environ.get("SHELL")
    user = os.getlogin()

    mem_total = ""
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if "MemTotal" in line:
                    mem_total = line.split()[1]
                    mem_total = int(mem_total) // 1024
    except FileNotFoundError:
        mem_total = "Unknown"

    total, used, free = shutil.disk_usage(home)
    total_gb = total // (2**30)
    used_gb = used // (2**30)

    ascii_logo = r"""

    .----. .----. .-.    .----.  .----.
    /  {}  \| {}  }| |   /  {}  \{ {__  
    \      /| .-. \| |   \      /.-._} }
    `----' `-' `-'`-'    `----' `----' 
    
    """


    print(f"{TEXT_COLOUR}{ascii_logo}")
    print(f"User: {username}")
    print(f"Host: {hostname}")
    print(f"OS: {system}")
    print(f"Python: {python_ver}")
    print(f"Memory: {mem_total} MB")
    print(f"Disk: {used_gb}GB / {total_gb}GB")
    print(f"Shell: {shell}")
    print(f"Release: {release}")
    print(f"User: {user} {RESET_COLOUR}")


# Creating functionality to access files from the host OS
# E.G. allows cd, mkdir, sudo, basically turns OrionOS into a terminal emulator until "exit" is ran

username = os.getlogin()
hostname = socket.gethostname()

PROMPT_COLOUR = "\033[34m"
TEXT_COLOUR = "\033[95m"
RESET_COLOUR = "\033[0m"

def syscontrol():
    print("Accessing host OS, type 'exit' to return to ORI OS.")
    home = os.path.expanduser("~")
    
    while True:
        username = os.getlogin()
        hostname = socket.gethostname()
        cwd = os.getcwd()

        if cwd == home:
            display_cwd = "~"
        elif cwd.startswith(home + os.sep):
            display_cwd = "~" + cwd[len(home):]
        else:
            display_cwd = cwd

        cmd = input(f"{PROMPT_COLOUR}{username}@OriOS-{hostname}{cwd}> {RESET_COLOUR}{TEXT_COLOUR}")

        if cmd.lower() == "exit":
            break
            
        if cmd.startswith("cd "):
            path = cmd.split(" ", 1)[1]
            try:
                os.chdir(path)
            except Exception as e:
                print("Error:", e)
        else:
            subprocess.run(cmd, shell=True)

# Defining a clear screen function
# I have no idea why theres a white line through "system"
# "If it works don't fiddle with it"

def clear():
    os.system("clear")



# Actually getting into the OS program now

print("\n###############################")
print("############ORION OS###########")
print("###############################\n")

# "syscontrol" will be partly unusable/unstable on windows.
    # It is meant for OrionOS to become a terminal emulator for linux distros
# "fastfetch" will be partly broken and return errors
    # Some gathered info uses linux-required functions.

def commands():
    print("Programs:\ncalculator (calc)" \
    "\nbrowser(browse)" \
    "\nclear (clear or ctrl+L)" \
    "\ncontrol host (syscontrol)" \
    "\nsystem info (fastfetch)" \
    "\nextra commands (extra)" \
    "\nquit ORION OS (Ctrl+C)" \
    "\ncommand list (--help)")

print("IF VIEWING ON GITHUB, PLEASE REVIEW THE COMMENTS ON LINE 136-139 FOR IMPORTANT INFO.")
print("Which program would you like to run? (run --help for a list of commands)")

# Opens up your PC's default browser (set new=2 to open in new tab, not new window)

def browse():
    webbrowser.open("https://www.google.com", new=1)


def music():
    webbrowser.open("https://www.spotify.com", new=1)

# Main Loop

while True:
    programRun = input(f"{PROMPT_COLOUR}{username}@OriOS-{hostname}> {RESET_COLOUR}{TEXT_COLOUR}")

    # From here downwards allows for adding commands, functions, etc.

    if programRun.lower() == "calc":
        print(f"{RESET_COLOUR}###############################")
        print(f"{RESET_COLOUR}###########CALCULATOR##########")
        print(f"{RESET_COLOUR}###############################\n")

        def calc():
            num1 = int(input(f"{RESET_COLOUR}{PROMPT_COLOUR}{username}@pyOS-{hostname}/calculator> {RESET_COLOUR}{TEXT_COLOUR} What is your first number? "))
            sign = input(f"{RESET_COLOUR}{PROMPT_COLOUR}{username}@pyOS-{hostname}/calculator> {RESET_COLOUR}{TEXT_COLOUR} What sign? (+ - / *) ")
            num2 = int(input(f"{RESET_COLOUR}{PROMPT_COLOUR}{username}@pyOS-{hostname}/calculator> {RESET_COLOUR}{TEXT_COLOUR} What is your second number? "))

            if sign == "+":
                result = num1 + num2
                print(f"{RESET_COLOUR}{TEXT_COLOUR}{num1} + {num2} = {result} {RESET_COLOUR}{TEXT_COLOUR}")
            elif sign == "-":
                result = num1 - num2
                print(f"{RESET_COLOUR}{TEXT_COLOUR}{num1} - {num2} = {result} {RESET_COLOUR}{TEXT_COLOUR}")
            elif sign == "/":
                result = num1 / num2
                print(f"{RESET_COLOUR}{TEXT_COLOUR}{num1} / {num2} = {result} {RESET_COLOUR}{TEXT_COLOUR}")
            elif sign == "*":
                result = num1 * num2
                print(f"{RESET_COLOUR}{TEXT_COLOUR}{num1} * {num2} = {result} {RESET_COLOUR}{TEXT_COLOUR}")
            else:
                print(f"{RESET_COLOUR}{TEXT_COLOUR}Error: option: invalid sign")

        calc()

    elif programRun.lower() == "browse":
        threading.Thread(target=browse).start()

    elif programRun.lower() == "extra":
        print(f"Extra commands:\necho\nwhoami\npwd\nmusic\n {RESET_COLOUR}{TEXT_COLOUR}")

    elif programRun.lower() == "echo":
        echoText = input("> ")
        print(echoText)

    elif programRun.lower() == "clear" or programRun.lower() == "\x0c":
        clear()
        continue

    elif programRun.lower() == "syscontrol":
        syscontrol()

    elif programRun.lower() == "--help":
        commands()

    elif programRun.lower() == "fastfetch":
        fastfetch()
    
    elif programRun == "exit":
        print("Error: exit: Unknown command. to quit ORION OS press ctrl+C. run --help for a list of commands.")

    elif programRun == "whoami":
        print(os.getlogin())
    
    elif programRun == "pwd":
        print(os.getcwd())

    elif programRun.lower() == "music":
        threading.Thread(target=music).start()


    # End of OS; Error message.

    else:
        print(f"Error: {programRun}: Unknown command. run --help for a list of commands")