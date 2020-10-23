#! /usr/bin/env python3

import sys
import os

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        os.system('./parser_comments.py ' + arg)
        # os.system('./parser.py ' + (arg + '.ou'))
    # os.system('rm *.ou')
