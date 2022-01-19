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

## Usage and Referencing

I would do something like the following:

Note: replace `.bashrc` with `.zshrc` or `.bash_profile`, etc., as necessary.

```
mkdir -p "$HOME/bin"
cd "$HOME/bin"
git clone https://github.com/phx/shell_utils
echo 'MY_BIN="$HOME/bin"' >> ~/.bashrc
echo 'SHELL_UTILS="$MY_BIN/shell_utils/bin"' >> ~/.bashrc
echo 'export PATH="$SHELL_UTILS:$MY_BIN:$PATH"' >> ~/.bashrc
source ~/.bashrc
```
