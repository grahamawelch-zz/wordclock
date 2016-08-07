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

For easy of debugging, start the script in screen so we can re-attach to it.

```
screen -R clock
sudo python clock.py 2> errors.txt
```

Then press `CTRL-A CTRL-D` to detach. Then you can always ssh back and run `screen -r clock` to see what the script is up to.

The script also redirects exceptions to `errors.txt` so you can investigate later.
