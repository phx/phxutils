# alarm

Linux Dependencies:
- `pulseaudio-utils`
- `libnotify-bin`

MacOS Dependencies:
- `coreutils` (installed via `brew`)

## Description:

This is a simple alarm clock script that I wrote, which I use on a daily basis in order to notify me for certain events.

I'm too lazy to figure out how to invoke Siri while already on a call, and I'd rather not go through the drudgery of manually setting up one-off alarms.

This little guy is super easy to use, but you can only set one alarm at a time.  That's all I need usually, or I will take more drastic measures like those listed above.

## Usage:

```
# Set alarm for 10am:
$ alarm 10am
setting alarm for Wed 19 Jan 2022 10:00:00 AM CST...

# Disable alarm:
$ alarm
alarm is off
```

In the above example, the sound file specified in the script will start playing on loop, and you will get a GUI alert every 5 seconds until the alarm is disabled.

### Cross-platform operation on MacOS:

As-is, the script is built to run on Linux, utilizing `paplay` for sounds and `notify-send` for GUI alerts.

I have put various comments in the script for use with MacOS:
- The native `afplay` command can be used in place of `paplay`
- The native `say` command can replace the reliance on the sound file
- The native `osascript` command can be used in place of `notify-send`

The most important dependency is the reliance on GNU `date` in order for this script to work properly.

GNU `date` can be downloaded on MacOS by installing `coreutils` via Homebrew, and is normally invoked using `gdate`, so you can either change the commands in the script to use `gdate` instead of `date`,
or you can just use GNU `date` by default on your system by doing something like the following:

```
brew install coreutils
sudo mv /bin/date /bin/bsd-date
sudo ln -s /usr/local/bin/date /bin/date
```
