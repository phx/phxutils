# ipgrep/cidrgrep

Dependencies:

- `/bin/sh`

`ipgrep` should grab all valid IPv4 addresses from stdin or a file: `0.0.0.0-255.255.255.255`

`cidrgrep` should do the same for IPv4 networks in CIDR notation: `0.0.0.0/0-255.255.255.255/32`

`ipportgrep` will grab IPv4 addresses (0.0.0.0/0) and port numbers (1-65535) in format: `1.2.3.4:12345`

All utilities leave IPs in the order they were found. Sorting can be done by piping to `sort -u`.

## Usage

`ipgrep [FILE]` or `[some command that returns scattered ips in output] | ipgrep`

`cidrgrep [FILE]` or `[some command that returns scattered ips in output] | cidrgrep`

`ipportgrep [FILE]` or `[some command that returns scattered ips in output] | ipportgrep`
