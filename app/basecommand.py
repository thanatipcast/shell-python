import sys
import os
import subprocess

class BaseCommand:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __str__(self):
        return f"{self.name} {self.args}"
    
    def __repr__(self):
        return f"{self.name} {self.args}"
    
    def execute(self):
        raise NotImplementedError(f"{self.__class__.__name__} does not implement execute()")
    
    # validate if a file name is a file and has access
    def _validate_file(self, file):
        path_env = os.environ.get("PATH","")
        path_split = path_env.split(os.pathsep)
        for directory in path_split:
            full_path = os.path.join(directory, file)
            if os.path.isfile(full_path) and os.access(full_path,os.X_OK):
                return full_path
            
        return None


# starts with exit
class ExitCommand(BaseCommand):
    def execute(self):
        sys.exit()


#starts with echo
class EchoCommand(BaseCommand):
    def execute(self):
        print(" ".join(self.args))

# starts with type
class TypeCommand(BaseCommand):
    shell_builtin = ["echo", "exit", "type", "pwd"]
    def execute(self):
        if len(self.args) == 0:
            return
        if self.args[0] in self.shell_builtin:
            print(f"{self.args[0]} is a shell builtin")
        else:
            self._find_file()

    def _find_file(self):
        full_path = self._validate_file(self.args[0])
        if full_path:
            print(f"{self.args[0]} is {full_path}")
        else:
            print(f"{self.args[0]} not found")

# starts with pwd

class PwdCommand(BaseCommand):
    def execute(self):
        current_path = os.getcwd()
        print(f"{current_path}")

# starts with nothing
class ExecuteCommand(BaseCommand):
    def execute(self):
        # search file then execute if found
        full_path = self._validate_file(self.name)
        if full_path:
            subprocess.run([self.name, *self.args])
        else:
            sys.stdout.write(f"{self.name}: command not found\n")   


# starts with cd
class CdCommand(BaseCommand):
    def execute(self):
        if len(self.args) == 0:
            return
        # absolute path
        if self.args[0]:
            try:
                os.chdir(self.args[0])
            except FileNotFoundError:
                print(f"cd: {self.args[0]}: No such file or directory")
