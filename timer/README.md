# timer

Linux Dependencies:
- `bash`
- `pulseaudio-utils`
- `libnotify-bin`

MacOS Dependencies:
- `bash`
- `coreutils` (installed via `brew`)

## Description:

Super simple timer script. Can use seconds, minutes, or hours, specified numerous ways:

```
timer 10s
timer 10seconds
timer 10 sec
timer 10 s
timer 10 seconds
timer 30m
timer 30 min
timer 30minutes
timer 3h
timer 3hr
timer 3hrs
timer 3 hours
...etc...
```
## Usage:

```
# Set alarm for 10am:
$ timer 10m
setting timer for 10 minute(s)...

# Disable timer:
$ timer
timer is off
```

In the above example, the sound file specified in the script will start playing on loop, and you will get a GUI alert every 5 seconds until the timer is disabled.

### Cross-platform operation on MacOS:

As-is, the script is built to run on Linux, utilizing `paplay` for sounds and `notify-send` for GUI alerts.

I have put various comments in the script for use with MacOS:
- The native `afplay` command can be used in place of `paplay`
- The native `say` command can alternately be used in place of `paplay` and replace the reliance on the sound file
- The native `osascript` command can be used in place of `notify-send`

The most important dependency is the reliance on GNU `date` in order for this script to work properly.

GNU `date` can be downloaded on MacOS by installing `coreutils` via Homebrew, and is normally invoked using `gdate`, so you can either change the commands in the script to use `gdate` instead of `date`,
or you can just use GNU `date` by default on your system by doing something like the following:

```
brew install coreutils
sudo mv /bin/date /bin/bsd-date
sudo ln -s /usr/local/bin/gdate /bin/date
```
