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


def wget_wrapper(args):
    print('emulating wget for ', ' '.join(args))
    status = 0
    raise(Exception('Not implemented'))
    return status


def generic_wrapper():
    args = sys.argv
    if len(args) <= 1:
        raise(Exception())
    if args[0].endswith('git-annex-wrapper'):
        del(args[0])
    if args[0].endswith('wget'):
        try:
            status = wget_wrapper(args)
        except Exception:
            print('Emulation failed, doing real call')
            status = fallthrough(args)
    else:
        status = fallthrough(args)
    return status
