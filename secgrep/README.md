# secgrep

A rough `grep` wrapper for interesting filenames that could potentially contain secrets.

Must be used on a file.  I'll update later with support for STDIN.

## Usage

```
secgrep <-d|--defluff> [/path/to/file]

[None]		searches for interesting files, then gets rid of any junk left over.
-d | --defluff	only gets rid of junk file output.
```

## Example

```
sudo find /home -type f 2>/dev/null | tee /tmp/paths.txt
secgrep /tmp/paths.txt
```
