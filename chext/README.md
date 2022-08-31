# chext

Dependencies:

- `/bin/sh`
- `sed` (any version)

`chext` is a command that simply renames extensions ending in [first argument] to extensions ending in [second argument] (only in the current directory).

This functionality may already be implemented in the `rename` command or something, but it was something I needed to use over and over again, so I wrote something myself.

I knew the exact functionality that I needed, and when I went to clone a git repo on my other computer, I decided that I needed	this functionality.

Instead of SSH'ing into my other computer and copying the function out of the functions file, sourced in my rc files, I decided to take a little extra time
to port it over to `phxutils`, which I will probably do with numerous other functions that could be useful not only to myself, but to others as well.

## Usage

`chext [old extension] [new extension]`

## Example

```
$ ls -lh
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 1.ps1
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 1.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 2.ps1
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 2.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 3.ps1
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 3.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 4.ps1
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 4.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 5.ps1
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 5.txt

$ chext ps1 jpg
renamed '1.ps1' -> '1.jpg'
renamed '2.ps1' -> '2.jpg'
renamed '3.ps1' -> '3.jpg'
renamed '4.ps1' -> '4.jpg'
renamed '5.ps1' -> '5.jpg'

$ ls -lh
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 1.jpg
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 1.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 2.jpg
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 2.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 3.jpg
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 3.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 4.jpg
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 4.txt
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 5.jpg
-rw-rw-r-- 1 phx phx 0 Aug 31 10:07 5.txt
```

## Why `chext` is better than other methods

After publishing `chext`, I got curious and wondered if there was a better way of accomplishing my goal.
After googling and coming upon [this Unix/Linux Stack Exchange question](https://unix.stackexchange.com/questions/19654/how-do-i-change-the-extension-of-multiple-files),
I have decided that my way is actually superior to any of the methods listed there. Let me explain...

**`rename` (`util-linux` version):**

```
rename [old_extension] [new_extension] *.[old_extension]
```

`rename` has the ability to do this via the command above, but only the [`util-linux`](https://en.wikipedia.org/wiki/Util-linux) version on Debian/Ubuntu.
A quick `command -v rename` told me that this utility was not even installed on my Ubuntu 20.04 system, so that was a no-go, because it relied on a non-native dependency.


**`rename` (`perl` version):**

```
rename "s/\.old_extension$/.new_extension/" *.old_extension
```

This version of `rename` is available on RHEL-based distros, and on MacOS, you would have to `brew install rename`, in order to utilize this command.

Thus we see why `rename` is not a valid option, because it is not cross-compatible between different *nix platforms.

**`zsh` shell built-in:**

```
zmv '(*).old_extension' '$1.new_extension'
```

This is nifty, but relies on `zsh`, which may not be installed on many systems, so it's a no for me, dawg.

**`bash` parameter expansion:**

```
for file in *.old_extension; do
  mv -- "$file" "${file%.old_extension}.new_extension"
done
```

This could potentially work, but it's not POSIX-compliant, so it couldn't be used in shell scripts or functions using shells like `sh` or `dash`.

**`sed` to the rescue:**

In its current implementation, `chext` only uses `/bin/sh` and literally any version of `sed`, whether it's GNU, BSD, etc., anything works.

This is the script in its entirety:

```
#!/bin/sh
old_ext="$1" 
new_ext="$2" 
for file in *.${old_ext}; do
  mv -v "$file" "$(echo "$file" | sed "s/.${old_ext}/.${new_ext}/g")"
done
```

...and I'm about to submit a new answer to the Stack Overflow question, because it wasn't listed as a possible solution in any of the answers.


