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

```
sudo apt-get install swig
sudo apt-get install scons
sudo apt-get install python-dev
sudo apt-get install vim
sudo apt-get install screen
sudo apt-get install gnome-schedule
```

Now follow instructions at http://popoklopsi.github.io/RaspberryPi-LedStrip/#!/ws2812


Jessie outputs audio over the pin we use to control the LED.
Try adding the following to your `/boot/config.txt`

```
hdmi_force_hotplug=1
hdmi_force_edid_audio=1
```

This might not be enough. Black list the Broadcom drivers as well.

```
cd /etc/modprobe.d
sudo vi alsa-blacklist.conf
```

Add the line `blacklist snd_bcm2835`, then reboot.

There are other gotchas to the circutry as well. See the section on "flickering randomly".
https://github.com/jgarff/rpi_ws281x/wiki

## Run the clock.

For easy of debugging, we will start the script in screen so we can re-attach to it.
Add the following lines to `sudo crontab -e`

```
@reboot bash /home/pi/workspace/wordclock/reboot.sh
```

You can always ssh back and run `sudo screen -r clock` to see what the script is up to.

The script also redirects exceptions to `errors.txt` so you can investigate later.

## Customize your Clock

Add some birthdays to a file called 'birthdays' in the format 'MONTH DAY', e.g. '2 3' for Feb 3rd.
Put each entry on its own line.

The threshold for what is considered hot or cold temperatures is set in [words.py](words.py).
The threshold for windy weather is set in the same file.
See WIND_CUTOFF, HOT_CUTOFF, and COLD_CUTOFF; units are MPH and F. (Defaults are 15, 90, 40)

You can also configure the colors used for holidays, or normal operation, in [words.py](words.py).

Based on how you layout your LEDs, you will need to update [light_map.py](light_map.py); [light_map_alt.py](light_map_alt.py) is an example alternative mapping of LEDs to words.

