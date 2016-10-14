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
            print('ANGQUICK: posix OS required.\n')
            exit(1)

    def prompt(self):
        newang_component = input('Angquick - New module name: ')
        print('prompt called')
        return newang_component

    def gen_new_component_files(self, name):
        module_path = name
        touch = 'touch '
        slash = '/'
        command_string = 'touch' + module_path + '/' + name

        os.mkdir(module_path)
        
        self.call(command_string + '.module.js')
        self.call(command_string + '.component.js')
        self.call(command_string + '.controller.js')
        self.call(command_string + '.html')
