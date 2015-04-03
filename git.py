#!/usr/bin/python

import sys
import os
import subprocess
import tempfile

######################
# audio player methods
######################


def is_exe(fpath):
    return os.path.isfile(fpath) and os.access(fpath, os.X_OK)


def which(program):
    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def audioplayer():
    for p in ('afplay', 'aplay', 'mpg123'):
        found = which(p)
        if found is not None:
            return found
    return None


def play(sound):
    player = audioplayer()

    if player:
        datapath = os.path.dirname(os.path.realpath(__file__))
        datapath = os.path.join(datapath, 'data')
        if not sound.endswith('.wav'):
            sound += '.wav'

        subprocess.Popen([player, os.path.join(datapath, sound)],
                         stdout=open(os.devnull, 'w'),
                         stderr=subprocess.STDOUT)


######################
# wrapper methods
######################

def what_sound(command):
    return {
        'clone': 'smb_kick',
        'checkout': 'smb_stomp',
        'add': 'smb_jump',
        'rm': 'smb_fireball',
        'commit': 'smb_1up',
        'push': 'smb_vine',
        'pull': 'smb_pipe',
        'tag': 'smb_pause',
    }.get(command, None)


def call_git(argv):
    argv.insert(0, 'git')

    try:
        with tempfile.NamedTemporaryFile() as temp:
            subprocess.check_call(argv)
    except subprocess.CalledProcessError as error:
        play('smb_die')
        return False

    return True

def main(argv):
    return_value = call_git(argv)

    if return_value:
        git_command = argv[0]
        sound = what_sound(git_command)
        if sound is not None:
            play(sound)


if __name__ == "__main__":
    main(sys.argv[1:])