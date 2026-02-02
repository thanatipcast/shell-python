import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True: 
        command = input("$ ")
        print("argv",sys.argv)
        print("argv1",sys.argv[1])
        print("argv2", sys.argv[2])
        if command == "exit":
            sys.exit()

        elif command:
            sys.stdout.write(f"{command}: command not found")
            print()
            continue   
   

if __name__ == "__main__":
    main()
