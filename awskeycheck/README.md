# awskeycheck

- Dependencies
  - `aws cli`
  - `jq`
  - `bash`

Checks validity of aws access/secret key combos.

```
Usage: awskeycheck [ -f [FILE CONTAINING CREDENTIALS] | <[AWS_ACCESS_KEY_ID] [AWS_SECRET_ACCESS_KEY]> ]

Options:
-f | --file	-f [FILE] will parse keys from file and rotate through them to check validity.
NONE		[AWS_ACCESS_KEY_ID] [AWS_SECRET_ACCESS_KEY] will check a single set of credentials passed as $1 and $2.

(will prompt if keys not provided)
```


