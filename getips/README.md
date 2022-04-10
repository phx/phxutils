# getips

Get all your interface names and their associated IPs when you are fed up with `ip` and/or `ifconfig`.

Want to get your WiFi IPv4 address in plain-text that can be easily piped or copied to the clipboard? Easy:

`getips wlan0`

Want to see all IPs associated with each active interface? Easy:

`getips`

Need your external IP? Simple:

`getips wan` or `getips ext`

The main `getips` command is extensible, as it returns all interfaces with IPs in JSON format, so it can be filtered via `jq` for whatever reason, if necessary.

## Example output

```
$ getips wlp2s0
192.168.1.15

$ getips -all wlp2s0
[
  "192.168.1.20",
  "fe80::3917:919a:1b2b:52c1"
]

$ getips
{
  "lo": [
    "127.0.0.1",
    "::1"
  ],
  "wlp2s0": [
    "192.168.1.15",
    "fe80::3917:919a:1b2b:52c1"
  ],
  "ipv6leakintrf0": [
    "fdeb:446c:912d:8da::",
    "fe80::43c3:3023:6fae:3e08"
  ],
  "docker0": [
    "172.17.0.1"
  ]
}  

$ getips wan
104.88.220.81
```
