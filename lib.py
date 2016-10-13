# angquick - Copyright by Brett Fraley 2016
# https://github.com/bFraley/angquick

import os

class AngQuick():
    def __init__(self):
        self.aq_text = 'angquick: '
        self.osname = os.name


    def call(self, shell_string):
        if os.system(shell_string):
            return True
        else:
            return False


    def check_posix(self):
        if not self.osname == 'posix':
            print('angquick currently only supports posix operating systems.\n')
            exit(1)
        else:
            print('\n{} {}'.format(self.aq_text, self.osname))
            return True


    def try_open_read(self, filename):

        try:
            fp = open(filename)
        except PermissionError:
            return "file permission error"
        else:
            with fp:
                return fp.readlines()


    def prompt(self):
        newang_component = input('Angquick - New component name: ')
        print('prompt called')
        return newang_component


    def gen_new_component_files(self, name):
        module_path = 'client/' + name
        touch = 'touch '
        slash = '/'
        command_string = touch + module_path + slash + name

        os.mkdir(module_path)
        
        self.call(command_string + '.module.js')
        self.call(command_string + '-page.component.js')
        self.call(command_string + '-page.controller.js')
        self.call(command_string + '-page.html')


# NOTES

"""
os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
"""


