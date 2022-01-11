# rlookup

Dependencies:

- `/bin/sh`
- `host` command (usually found in `dns-utils`, `bind-utils`, or `bind9-utils`

`rlookup` is a utility that performs reverse lookups on IP addresses and returns
a comma-separated list of IPs and their respective DNS entries, only for the IPs
that have valid DNS mappings.

It can be used against a list of IPs or take stdin from a pipe.

## Usage

`rlookup [file with list of ips]` or `[command generating ip list] | rlookup`
