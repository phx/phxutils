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
