'''
By eroen, 2013

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.
'''

import argparse
import os.path
import sys
import subprocess


def fallthrough(args):
    proc = subprocess.Popen(args)
    return proc.wait()


def wget_wrapper(args):
    print('emulating wget for ', ' '.join(args))
    if args[0].endswith('wget'):
        args = args[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('-O')
    parser.add_argument('-t')
    parser.add_argument('-T')
    parser.add_argument('--passive-ftp', action='store_true')

    wgetargs = parser.parse_args(args)
    src = wgetargs.src
    out = wgetargs.O
    (repo, outfile) = os.path.split(out)

    print('source: ', src)
    print('repo: ', repo)
    print('outfile: ', outfile)

    os.chdir(repo)
    proc = subprocess.Popen(['git', 'annex', 'whereis', outfile],
                            stdout=subprocess.PIPE)
    (stdoutdata, _) = proc.communicate()
    print('\n'.join(stdoutdata.decode().split()))

    if not 'ok' in stdoutdata.decode().split():
        raise(Exception())

    proc = subprocess.Popen(['git', 'annex', 'get', outfile],
                            stdout=subprocess.PIPE)
    (stdoutdata, _) = proc.communicate()
    print('\n'.join(stdoutdata.decode().split()))
    status = proc.returncode

    return status


def generic_wrapper():
    args = sys.argv
    if len(args) <= 1:
        raise(Exception())
    if args[0].endswith('git-annex-wrapper'):
        args = args[1:]
    if args[0].endswith('wget'):
        try:
            status = wget_wrapper(args)
        except Exception as exc:
            print(exc)
            print('Emulation failed, doing real call')
            status = fallthrough(args)
    else:
        status = fallthrough(args)
    return status
