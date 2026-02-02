import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True: 
        command = input("$ ")
        command_split = command.split()
        command_name = command_split[0]
        args = command_split[1:]
        shell_builtin = ["echo", "exit", "type"]
        if command_name == "exit":
            sys.exit()
        elif command_name == "echo":
                print(" ".join(args))
        elif command_name == "type":
            if args[0] in shell_builtin:
                print(f"{args[0]} is a shell builtin")
            else:
                print(f"{args[0]}: not found")

        elif command:
            sys.stdout.write(f"{command}: command not found")
            print()
            continue   


if __name__ == "__main__":
    main()
