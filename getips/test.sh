#!/bin/sh

active_ifaces="$(ifconfig | grep -E '^[a-z]+[0-9]+: flags=' | awk -F ': ' '{print $1}')"

for iface in $(echo "$active_ifaces"); do
  ifname="$(ifconfig "$iface" | grep -E '^[a-z]+[0-9]+: flags=' | awk -F ': ' '{print $1}')"
  ipv4s="$(ifconfig "$iface" | grep inet | grep -v inet6 | cut -d' ' -f2)"
  ipv6s="$(ifconfig "$iface" | grep inet6 | cut -d' ' -f2)"
  if ifconfig "$iface" | grep status | grep -q active; then
    if [ ! -z "$ipv4s" ] || [ ! -z "$ipv6s" ]; then
      echo "name: $ifname"
      echo "$ipv4s"
      echo "$ipv6s"
      echo ----------------------------------------------
    fi
  fi
done
