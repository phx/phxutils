# snap-upgrade

A utility to immediately upgrade all snaps by killing them if they are running and then upgrading them.

No idea why this feature isn't available natively.  The notifications kill me.  This is to just go ahead and do the damn thing.

## Requirements

- Linux
- `snapd`
- `bash`

## Usage

Run with `-y` or `-f` to prevent user input that confirms whether or not to kill the necessary processes.

This is because it can be destructive if you're in the middle of something.

If you know you want to upgrade everything immediately, just run `snap-upgrade -y`.
