# enc

Dependencies:

- bash
- python3
- openssl
- iconv

This is a shortcut program I created to generate different types of encodings
for different purposes.  Each time I work with a new encoding for an extended
period of time, I will tend to add it to the program, so this program will
continue to be updated periodically.

## Usage (at time of writing):

```

enc [type] [content]|[-f filename]
or
enc [-t <type> -o <options> <-d> -c [content]

-t|--type	type of encoding (see encoding types below)
-o|--options	[not currently implemented]
-d|--decode	decode instead of encode
-c|--content	everything after -c will be processed (should be quoted, last param)
-h|--help	show this help output

Encoding Types:

- Quoting:
  dquote	return content surrounded by double quotes
  undquote	remove content's surrounding double quotes
  squote	return content surrounded by single quotes
  unsquote	remove content's surrounding single quotes
  psesc		powershell escape quoting

- Base64:
  b64		base64 single line (cross-platform)
  b64m		base64 multi-line (*nix)
  b64wm		base64 multi-line (windows)
  b64u		base64 unicode single line (cross-platform)
  b64um		base64 unicode multi-line (*nix)
  b64wum	base64 unicode multi-line (windows)

- Miscellaneous:
  u2d		unix2dos (LF -> CRLF)
  d2u		dos2unix (CRLF -> LF)
  url		urlencoded
  oneliner	combine multi-line command into one-liner

```
