import sys
import os
from basecommand import (
    BaseCommand,
    EchoCommand,
    ExitCommand,
    TypeCommand,
    ExecuteCommand
)

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True: 
        command = input("$ ")
        command_split = command.split()
        if len(command_split) == 0:
            continue
        command_name = command_split[0]
        args = command_split[1:]

        c = command_mapper(command_name, args)
        c.execute()

def command_mapper(command_name, args) -> BaseCommand:
    match command_name:
            case "exit":
                c = ExitCommand(command_name, args)
            case "echo":
                c = EchoCommand(command_name, args)
            case "type":
                c = TypeCommand(command_name, args)
            case _:
                c = ExecuteCommand(command_name, args)
    return c
    

if __name__ == "__main__":
    main()

