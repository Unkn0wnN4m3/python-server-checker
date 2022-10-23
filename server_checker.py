import socket

from colorama import Fore, Style, init


def is_running(site: str) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False


if __name__ == "__main__":
    init()

    while True:
        site = input("Website to connect: ")

        if is_running(site):
            print(Fore.GREEN + f"\n{site} is running!")
        else:
            print(Fore.RED + f"\nThere is a problem with {site}")

        print(Style.RESET_ALL)

        if input("Would you like to check another website? [Y/n]: ") in {
                "n", "N"
        }:
            break
