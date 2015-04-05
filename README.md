This is a small wrapper around git that plays sounds effects from Super Mario Bros (NES) on common commands.
Heavily inspired by Sean Farley's implementation for mercurial (https://bitbucket.org/seanfarley/smb/src)

If you have any ideas about how to package and distribute this project (I'm relatively new to python), please feel free to open an issue!

# Sounds for commands

- clone: kick
- checkout: stomp
- add: jump
- rm: fireball
- commit: 1up
- push: vine
- pull: pipe
- tag: pause
- error: die

# Installation

## Homebrew

1. Tap my homebrew tap: ```$ brew tap pascaldevink/pascaldevink```
2. Update brew: ```$ brew update```
3. Install git-smb: ```$ brew install git-smb```
4. Bonus: put ```alias git=git-smb``` somewhere in your (ba)(z)(k)sh profile to make the wrapping complete and easy

## Manual

1. Clone or download this repository.
2. Either put the bin folder in your path or create a symlink to it (eg. in /usr/local/bin)
3. You can now use it with ```$ git-smb```
4. Bonus: put ```alias git=git-smb``` somewhere in your (ba)(z)(k)sh profile to make the wrapping complete and easy
