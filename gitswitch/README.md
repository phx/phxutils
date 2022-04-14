# gitswitch

Dependencies:

- `/bin/sh`
- `git`

Easy method for managing multiple `git` identities without changing your normal git paths/commands/configs/etc.

Run `gitswitch init`, and update `~/.config/gitswitch/config.ini` as necessary to include your preferred ssh keys, names, and emails.

This script can be improved upon further to swap by profile name, but for my personal use case and the sake of simplicity, I will simply switch between 2 identities.

**NOTE:** This script uses `git config --global user.name` and `git config --global user.email`.  If you prefer, feel free to alter the script to not use the `--global` flag.

## Requirements:

Included in `~/.ssh/config`:

```
# BEGIN GIT
Host github.com
  HostName github.com
  User git
  IdentityFile /path/to/rsa_private_key
# END GIT
```

(or whatever git server you are using - just make sure the comments are there.)


### `gitswitch help` output:

```

Usage: gitswitch <init>|<example>|<help>

Optional arguments:
help		shows this help text
init		creates the example configuration at ~/.config/gitswitch/config.ini
example		shows the example gitswitch configuration

*** IMPORTANT ***
Make sure you have the '# BEGIN GIT' and '# END GIT' comments in '~/.ssh/config'.

~/.ssh/config should contain something like the following:

# BEGIN GIT
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
# END GIT

1. modify ~/.ssh/config as stated above.
2. run 'gitswitch init' to copy example information to ~/.config/gitswitch/config.ini
3. modify ~/.config/gitswitch/config.ini to reflect your account information
4. run 'gitswitch' to switch between git users

```
