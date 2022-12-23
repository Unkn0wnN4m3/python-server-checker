import argparse
import socket

from colorama import Fore, Style, init


def main():
    custom_timeout = 3
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    parser = argparse.ArgumentParser(
        prog="Server Checker",
        description="A server status checker",
    )

    parser.add_argument("hostname",
                        help="Introduce a valid hostname [example.com]")

    parser.add_argument("--port",
                        "-p",
                        type=int,
                        default=80,
                        help="Introduce a valid port [80]: --port <integer>")

    args = parser.parse_args()

    init()

    try:
        sock.settimeout(custom_timeout)
        sock.connect((args.hostname, args.port))
    except Exception:
        print(Fore.RED + '\nCheck if hostname or port are correct')
    else:
        print(Fore.GREEN + f'\n> {args.hostname} is running!')
        sock.close()

    Style.RESET_ALL


if __name__ == '__main__':
    main()
