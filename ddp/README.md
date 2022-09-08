# ddp

Optional Dependencies:

- 'pv'
- 'dialog'

`ddp` is a wrapper for `dd` that shows progress without having to remember `pv` commands.  If you have both `pv` and `dialog` installed,
you will see a nice dialog progess bar.  If you only have `pv` installed, you will see the `pv` progress bar in the terminal.  If neither
`pv` nor `dialog` are installed, this wrapper will default to plain `dd` with `status=progress`.

## Usage

```
Usage: ddp [input_file] [output_file] <block_size> <additional_options>

Defaults:
block size 		4096
additional options	conv=notrunc,noerror,fsync

Details:
If pv or dialog is not installed, then the following default command will be issued:
sudo dd if=[input_file] of=[output_file] bs=4096 conv=notrunc,noerror,fsync status=progress
^ block size and additional options (except for 'status=progress') can be overridden by cli arguments.
If your version of 'dd' does not support 'status=progress', then JUST USE 'dd' INSTEAD!
```
