# timer

Linux Dependencies:
- `bash`
- `pulseaudio-utils`
- `libnotify-bin`

MacOS Dependencies:
- `bash`

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
