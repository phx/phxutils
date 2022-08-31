# chext

Dependencies:

- `bash`

`chext` is a command that simply renames extensions ending in [first argument] to extensions ending in [second argument] (only in the current directory).

This functionality may already be implemented in the `rename` command or something, but it was something I needed to use over and over again.

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

### This is literally the entire "script":

```
old_ext="$1" 
new_ext="$2" 
for i in *.${old_ext}; do
  mv -v "$i" "$(echo "$i" | sed "s/.${old_ext}/.${new_ext}/g")"
done
```
