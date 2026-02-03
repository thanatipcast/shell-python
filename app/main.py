import sys
import os

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
        elif command_name == "type" and len(args) == 1:
            #TODO bug on command "type"
            if args[0] in shell_builtin:
                print(f"{args[0]} is a shell builtin")
            else:
                found = False
                path_env = os.environ.get("PATH","")
                path_split = path_env.split(os.pathsep)
                for directory in path_split:
                    full_path = os.path.join(directory,args[0])
                    full_path = full_path + ".exe"
                    print("full_path", full_path)
                    if os.path.isfile(full_path) and os.access(full_path,os.X_OK):
                        print(f"{args[0]} is {full_path}")
                        found = True
                        break       
                if not found:
                    print(f"{args[0]}: not found")

        elif command:
            sys.stdout.write(f"{command}: command not found")
            print()
            continue   


if __name__ == "__main__":
    main()
