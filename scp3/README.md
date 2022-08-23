# scp3

Dependencies: `scp`

`scp3` can be used when `scp -3` is unavailble or is acting wonky.  It copies a file or directory from one host to another simply by first staging the target file or directory
in a temporary location on your current host.  If I understand the functionality of `scp -3` correctly, `scp3` will take twice as long for file transfers because of the middle (staging)
step, but it provides very good informational output, and I use it often, because `scp -3` usually fails me for some reason.

An additional feature of `scp3` is the ability to copy the initial file or directory (1st argument) to multiple hosts/locations (every argument after 1st argument).
If you don't have SSH public key auth enabled, you will be prompted for the SSH user password for each host without key-based auth enabled.

## Usage

```
scp3 user@host_A:/path/to/target_file_or_dir user@host_B:/path/to/destination_file_or_dir [user@host_C:/path/to/destination_file_or_dir] ...
```

## Example output

```
scp3 "root@10.0.5.100:/usr/local/opnsense/build/22.7/amd64/images/OPNsense-202208231312-OpenSSL-dvd-amd64.iso" "root@192.168.1.8:/vmfs/volumes/SSD-RAID-10/ISO/opnsense_22.7_20220823.iso" "phx@localhost:/home/phx/Downloads/opnsense.iso"

staging root@10.0.5.100:/usr/local/opnsense/build/22.7/amd64/images/OPNsense-202208231312-OpenSSL-dvd-amd64.iso to /tmp/tmp.vVatkNVspy/OPNsense-202208231312-OpenSSL-dvd-amd64.iso...
OPNsense-202208231312-OpenSSL-dvd-amd64.iso                                                                                                                                        100% 1345MB  65.0MB/s   00:20    
uploading /tmp/tmp.vVatkNVspy/OPNsense-202208231312-OpenSSL-dvd-amd64.iso to root@192.168.1.8:/vmfs/volumes/SSD-RAID-10/ISO/opnsense_22.7_20220823.iso...
OPNsense-202208231312-OpenSSL-dvd-amd64.iso                                                                                                                                        100% 1345MB  26.6MB/s   00:50    
uploading /tmp/tmp.vVatkNVspy/OPNsense-202208231312-OpenSSL-dvd-amd64.iso to phx@localhost:/home/phx/Downloads/opnsense.iso...
OPNsense-202208231312-OpenSSL-dvd-amd64.iso                                                                                                                                        100% 1345MB 199.6MB/s   00:06    
cleaning up...
removed '/tmp/tmp.vVatkNVspy/OPNsense-202208231312-OpenSSL-dvd-amd64.iso'
removed directory '/tmp/tmp.vVatkNVspy'
done.

```

### Contributing

If you wish to expand on this script to enable `-i` to specify which SSH key to use or add options to speed it up by using GNU `parallel`, subshells, or some other type of parallel processing,
simply submit a pull request.  Otherwise, I'm happy with this tool the way it is, because it fits most of my use cases.
