# asntocidr

Requirements:
- `/bin/sh`
- `whois`

This script will take stdinput via a pipe, file(s) as arguments, or AS Numbers as arguments, and will return the CIDR network ranges associated with those ASNs.

## Examples:

```
$ cat asns.list
AS39577
AS49184
AS49140
```

The following 3 commands will all return the same output.

```
$ cat asns.list | asntocidr
$ asntocidr asns.list
$ asntocidr AS39577 AS49184 AS49140
```

Output:

```
185.230.243.0/24
194.60.242.0/24
91.226.137.0/24
93.171.96.0/23
93.171.96.0/24
93.171.97.0/24
93.170.3.0/24
195.88.192.0/23
```

