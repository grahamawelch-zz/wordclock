# wordclock
A simple word clock using an individually addressable LED strip and Raspberry Pi Zero

## Setup your Pi

- Edit `/etc/network/interfaces`
- Change the line `iface wlan0 inet manual` to `iface wlan0 inet dhcp`
- Edit `/etc/wpa_supplicant/wpa_supplicant.conf`
- Prepoulate some Wifi network SSIDs and passwords. It might be a good idea to add the following fallback as well. Use `key_mgmt=NONE` for open networks.
```
network={
  ssid="wordclock-fallback"
  psk="fallbackpassword"
  priority=10
}
```

Once this is set up, the Pi should automatically connect to the highest priority network it can find.

From there, `ssh pi@raspberrypi.local` with the password `raspberry`.
