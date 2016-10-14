# angquick - lib.py
# https://github.com/bFraley/angquick

import os

class AngQuick():
    def __init__(self):
        self.osname = os.name
        self.file_extensions = [
            '.module.js',
            '.component.js',
            '.controller.js',
            '.html'
        ]

    # Execute shell commands.
    def call(self, shell_string):
        if os.system(shell_string):
            return True
        else:
            return False

    # Check for compatible OS.
    def check_posix(self):
        if not self.osname == 'posix':
            print('angquick: posix OS required.\n')
            exit(1)

    def gen_new_component_files(self, name):
        module_path = name
        touch = 'touch '
        command_string = touch + module_path + '/' + name
        os.mkdir(module_path)

        for ext in self.file_extensions:
            self.call(command_string + ext)
        