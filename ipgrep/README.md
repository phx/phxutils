# ipgrep

Dependencies:

- `/bin/sh`

`ipgrep` will grab all IPv4 addresses from stdin or a file.

It's a simple alternative always having to type `grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}` (and is actually more accurate, by only targeting `0.0.0.0-255.255.255.255`.

It leaves IPs in the order they were found. Sorting can be done by piping to `sort -u`.

## Usage

`ipgrep [FILE]` or `[some command that returns scattered ips in output] | ipgrep`
