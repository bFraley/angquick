import os

class Check():
    def __init__(self):
        self.osname = os.name

    def get_osname(self):
        if not self.osname == 'posix':
            print('angquick currently only supports posix operating systems.\n')
            exit(1)
        else:
            return self.osname