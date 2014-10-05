import configparser
import os
import string
import cmd2
from termcolor import colored
from progressbar import ProgressBar, Bar

class FimafengConsole(cmd2.Cmd):

    config = ''

    def __init__(self, config):
        self.config = config
        cmd2.Cmd.__init__(self)


if __name__ == '__main__':
    config = configparser.RawConfigParser()
    console = FimafengConsole(config)
    console.cmdloop()
