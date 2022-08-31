# phxutils

This is going to be a handy little repo where I maintain some of useful scripts
that I use on a regular basis.  I have a private repo where I have maintained
most of these scripts for a long time, but some of them could prove useful to the
general public, and half the time I forget what they do and end up re-writing them.

This repo will be a place for me to keep them up-to-date and document what they do.

Some aren't even big enough to be called scripts and are more like bash/zsh functions,
but it's easier having the commands at my fingertips by having all my tools installed
instead of finding/copy/pasting functions into my `~/.bashrc`/`~/.zshrc`.

The structure includes an individual folder for each script with a `README.md` documenting
what the script does.  Additionally, there will be a `bin` directory where I will symlink
all of the actual scripts for easy importing into your `$PATH`.

This project is also maintained on PyPi for easy installation via `pip`.

For more information, browse to the subfolders to view the individual README files.

I will continue to add scripts to this repo as I have time and as the need for them arises.

## Requirements:

In order to fully-utilize all of the scripts included in `phxutils`, Linux is a pre-requisite, but many will work on MacOS (some may need to be tweaked a bit).

To view individual requirements, feel free to view each package's README file.

The following additional requirements are necessary:

- `/bin/sh` (many scripts)
- `bash` (some scripts)
- `python3` (some scripts)

## Simple Installation via pip

Installation is extremely simple using [`pip`](https://pip.pypa.io/en/stable/installation/):

Install from [PyPi](https://pypi.org/project/phxutils/):

`pip3 install --user phxutils`

or install latest version from GitHub:

`pip3 install --user git+https://github.com/phx/phxutils`

For what it's worth, most of the `phxutils` scripts use `sh` and `bash`.

The only Python scripts at the time of this writing are Python3, and are executable with hashbangs pointing to `/usr/bin/env python3` and only use the standard library.

This means, you won't clutter your native Python intallation by installing a bunch of third party libraries outside of virtual environments.

### Upgrading via pip

`pip3 install --upgrade --user phxutils`

or

`pip3 install --upgrade --user git+https://github.com/phx/phxutils`

### Uninstall

`pip3 uninstall phxutils`

## Advanced Installation

To add these programs to your `$PATH` without using `pip3`, I would do something like the following:

Note: replace `.bashrc` with `.zshrc` or `.bash_profile`, etc., as necessary.

```
mkdir -p "$HOME/bin"
cd "$HOME/bin"
git clone https://github.com/phx/phxutils
echo 'PHX_UTILS="$HOME/bin/phxutils/bin"' >> ~/.bashrc
echo 'export PATH="$PHX_UTILS:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

The benefits to this method are an easier upgrade.

### Easy Upgrade via Advanced Install Method

`cd "$HOME/bin/phxutils" && git pull`

### Uninstall

`sed -i '/PHX_UTILS/d' ~/.bashrc && rm -rf "$HOME/bin/phxutils"`

Note: replace `.bashrc` with `.zshrc` or `.bash_profile`, etc., as necessary in the above command.

