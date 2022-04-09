# ipgrep/cidrgrep

Dependencies:

- `/bin/sh`

`ipgrep` should grab all valid IPv4 addresses from stdin or a file: `0.0.0.0-255.255.255.255`

`cidrgrep` should do the same for IPv4 networks in CIDR notation: `0.0.0.0/8-255.255.255.255/32`

They leave IPs in the order they were found. Sorting can be done by piping to `sort -u`.

## Usage

`ipgrep [FILE]` or `[some command that returns scattered ips in output] | ipgrep`

`cidrgrep [FILE]` or `[some command that returns scattered ips in output] | cidrgrep`
