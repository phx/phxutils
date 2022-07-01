# selfsign

Dependencies:

- OpenSSL

This script will generate a passwordless self-signed certificate with the domain name specified in the first argument or passed as the `$FQDN` environment variable.

By default, it will write the keyfile and certfile to the current working directory, but a different directory can be specified by passing the `$OUTPUTDIR` environment variable.

## Example:

$ selfsign '*.example.com'

Generating a RSA private key
...............................................................................................................................................................................................................................................++++
.........................++++
writing new private key to '/path/to/wildcard.example.com.key'
-----
-rw-rw-r-- 1 phx phx 1.8K Jul  1 14:51 /path/to/wildcard.example.com.crt
-rw------- 1 phx phx 3.2K Jul  1 14:51 /path/to/wildcard.example.com.key
