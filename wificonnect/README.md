# wificonnect

Dependencies:

- `bash`
- `sudo`
- `NetworkManager`
- `nmcli`

This is a wrapper for `nmcli` with simpler syntax that makes it easier to connect to wifi networks, especially hidden ones.

## Usage

```
wificonnect <-s SSID -p PASSWORD <-i INTERFACE> <-H|--hidden> >

Options:

-s | --ssid SSID
-p | --pass PASSWORD
-i | --interface IFACE (default: wlp2s0)
-H | --hidden (default: false)

If run without parameters, wificonnect will list details about the wifi networks currently available.
Parameters can also be set using environment variables and passing dummy arguments.
```
