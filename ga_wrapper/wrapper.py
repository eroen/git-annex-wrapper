'''
By eroen, 2013

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.
'''

import sys
import subprocess


def fallthrough(args):
    proc = subprocess.Popen(args)
    return proc.wait()


def generic_wrapper():
    args = sys.argv
    if args[0].endswith('git-annex-wrapper'):
        del(args[0])
    return fallthrough(args)
