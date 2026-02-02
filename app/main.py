import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True: 
        command = input("$ ")
        if command:
            sys.stdout.write(f"{command}: command not found")
            print()
            continue
    #display prompt $
    #user input
    #print out command not found
    #return to display prompt

if __name__ == "__main__":
    main()
