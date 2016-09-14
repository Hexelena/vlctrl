# vlctrl
D-Bus remote for vlc.  
Xfce doesn't bring native support for the media control keys (play, pause, stop, next, previous) on thinkpads.  
So i wrote a script that utilizes the D-Bus interface of vlc to enable the media keys.  
Note: The keys work if vlc has focus but not globally, also i am using Xfce 4.10.1.

Also, if you are trying to call D-Bus methods and get properties with python and the dbus module this is a possible place to start.

## How can i use this?
Clone the repository and make vlctrl.py executable(`chmod +x vlctrcl.py`)
Then just run the script with the necessary flags: 

####Usage: vlctrl.py [options]
#####important options:
```
  -l, --play        tell vlc to start playback  
  -t, --play-pause  tell vlc to toggle between play and pause  
  -a, --pause       tell vlc to pause playback  
  -s, --stop        tell vlc to stop playback  
  -n, --next        tell vlc to play the next track  
  -p, --prev        tell vlc to play the previous track  
  -q, --quiet       don't print error messages  
```
####Example:
Now you can create a new keyboard shortcut with the command of `/path/to/script/vlctrl.py -q -t` to toggle playback and map it to your play button.

## I don't use vlc, can i still use the script?
Download a D-Bus debugger (e.g. `d-feet`) and search for your media player under `'org.mpris.MediaPlayer.yourplayername'`.
Change the initialization in [vlctrl.py line 14](vlctrl.py#L14) to the media player of your choice.  
Most other players support the `'org.mpris.MediaPlayer2.Player'` interface so that should make it work.  
If you run into problems just open an issue.

## Links:
#### (btw I think there should be a way to use this universal with all supported media players. Tell me if you found it ;-) )
* [get and set properties (on music players) with the python dbus interface](https://stackoverflow.com/questions/9493494/mpris-python-dbus-reading-and-writing-properties)
* [first useful link i found about controlling vlc from the command line via D-Bus](https://theelitist.github.io/control-vlc-media-player-through-d-bus/)
* [Google Code site with the code that inspired me to try to control vlc with python and dbus](https://code.google.com/archive/p/mediakeys-daemon/downloads). The script would be useful if you have a gnome session running - buuuut Xfce is not gnome !!
