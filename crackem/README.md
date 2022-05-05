# crackem

Requirements:

- `hashcat`
- `bash`

This is a simple wrapper for `hashcat`.

We don't use it regularly, but when we do, we completely forget how to use it.

This makes that easier.

## Usage

```
USAGE: crackem -t hashtype -r rules_file -i input_file -o output_file -l wordlist

Parameters:
-t | --hashtype		hash type code
			default: 1000 (NTLM)
			['crackem -ls' to view all hash codes]

-r | --rulesfile	hashcat rules file to implement
			default: OneRuleToRuleThemAll.rule

-i | --inputfile	path to list of hashes
			default: hashes.txt

-o | --outputfile	path to output file
			default: cracked.txt

-l | --wordlist		path to password list
			default: rockyou.txt

Boolean Options:
-ls  | --list-codes	list all hash type codes with associated hash type names
-D   | --default	run with default options listed above
-1   | --onerule	download OneRuleToRuleThemAll.rule
-64  | --best64		download best64.rule
-ru1 | --rockyou	download rockyou.txt.gz and gunzip
-ru2 | --rockyou-2021	get links to download RockYou2021.txt.gz
-k   | --kaonashi	get links to download Kaonashi lists
-h   | --help		show this help text
```
