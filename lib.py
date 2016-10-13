import os

class AngQuick():
    def __init__(self):
        self.aq_text = 'angquick: '
        self.osname = os.name


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
            return "some default data"
        else:
            with fp:
                return fp.readlines()

    def prompt(self):
        newang_component = input('Angquick - New component name: ')
        print('prompt called')
        return newang_component



# NOTES

"""
os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
"""


