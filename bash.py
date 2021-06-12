import os
import colorama
import socket
import ctypes

inner = "continue"

while inner != "exit":
    print(colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX + os.getlogin() + "@" + socket.gethostname() + colorama.Style.RESET_ALL + ":" + colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX + os.getcwd().replace("/home/" + os.getlogin(), "~") + colorama.Style.RESET_ALL, end="")
    try:
        if os.geteuid() == 0:
            print("#", end=" ")
        else:
            print("$", end=" ")
    except AttributeError:
        if ctypes.windll.shell32.IsUserAnAdmin():
            print("#", end=" ")
        else:
            print("$", end=" ")
    inner = input()
    code = os.system(inner)
    if code:
        print(colorama.Fore.RED + "Error code : " + str(code))
    if inner:
        print()
