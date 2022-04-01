# shell_utils

This is going to be a handy little repo where I maintain some of useful scripts
that I use on a regular basis.  I have a private repo where I have maintained
most of these scripts for a long time, but some of them could prove useful to the
general public, and half the time I forget what they do and end up re-writing them.

This repo will be a place for me to keep them up-to-date and document what they do.

The structure that I'm going to try to create will be an individual folder for each
script with a `README.md` documenting what the script does.  Additionally, there
will be a `bin` directory where I will try to symlink all of the actual scripts
for easy importing into your `$PATH`.

For more information, browse to the subfolders to view the individual README files.

I will continue to add scripts to this repo as I have time and as the need for them arises.

## Requirements:

In order to fully-utilize all of the scripts included in `shellutils`, Linux is a pre-requisite, but many will work on MacOS (but some may need to be tweaked a bit).

To view individual requirements, feel free to view each package's README file.

The following additional requirements are necessary:

- `/bin/sh` (many scripts)
- `bash` (some scripts)
- `python3` (some scripts)

## Simple Installation via pip

Installation is extremely simple using [`pip`](https://pip.pypa.io/en/stable/installation/):

`pip3 install --user git+https://github.com/phx/shellutils`

For what it's worth, most of the `shellutils` scripts use `sh` and `bash`.

The only Python scripts at the time of this writing are Python3, and are executable with hashbangs pointing to `/usr/bin/env python3` and only use the standard library.

This means, you won't clutter your native Python intallation by installing a bunch of third party libraries outside of virtual environments.

This also means that it shouldn't matter what version of `pip` you use, since it's just using the `setuptools` module.
That being said, I would always recommend `pip3`, or better yet, using `python3 -m pip` rather than `pip3`.

Just try to remember to use the same version of `pip` for uninstalling or upgrading.

### Upgrading via pip

`pip3 install --user --upgrade git+https://github.com/phx/shellutils`

### Uninstall

`pip3 uninstall shellutils`

## Advanced Installation

To add these programs to your `$PATH` without using `pip3`, I would do something like the following:

Note: replace `.bashrc` with `.zshrc` or `.bash_profile`, etc., as necessary.

```
mkdir -p "$HOME/bin"
cd "$HOME/bin"
git clone https://github.com/phx/shellutils
echo 'SHELL_UTILS="$HOME/bin/shellutils/bin"' >> ~/.bashrc
echo 'export PATH="$SHELL_UTILS:$MY_BIN:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

The benefits to this method are an easier upgrade.

### Easy Upgrade via Advanced Install Method

`cd "$HOME/bin/shellutils" && git pull`

### Uninstall

`sed -i '/SHELL_UTILS/d' ~/.bashrc && rm -rf "$HOME/bin/shellutils"`

Note: replace `.bashrc` with `.zshrc` or `.bash_profile`, etc., as necessary in the above command.

