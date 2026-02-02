import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True: 
        command = input("$ ")
        command_split = command.split()
        command_length = len(command_split)
        command_name = command_split[0]
        args = command_split[1:]
        if len(command_split) == 1:
            if command == "exit":
                sys.exit()
        elif command_length > 1:
            if command_name == "echo":
                    print(" ".join(args))
            elif command:
                sys.stdout.write(f"{command}: command not found")
                print()
                continue   
   

if __name__ == "__main__":
    main()
