#! /usr/bin/env python3

import dbus

from optparse import OptionParser



class VlcTalker:
    def __init__(self): 
        self.session = dbus.SessionBus()
        self.vlc_dbus_obj = None
        try:
            self.vlc_dbus_obj = self.session.get_object('org.mpris.MediaPlayer2.vlc', '/org/mpris/MediaPlayer2')
        except dbus.exceptions.DBusException as dbex:
            print(dbex.get_dbus_message())
            if dbex.get_dbus_message() == 'The name org.mpris.MediaPlayer2.vlc was not provided by any .service files':
                print('--> the program is unable to find a running vlc instance in the dbus interface')
            else:
                print('--> an unknown error occured. Try to run the following command in you command line to test ' + 
                    'if vlc control via dbus is working (it should pause current playback):\n\n\t{}\n'.format(
                    'dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause'))
                

    def get_playstate(self):
        # TODO: check if there needs to be some cleanup here.
        props_interface = dbus.Interface(self.vlc_dbus_obj, 'org.freedesktop.DBus.Properties')
        return props_interface.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')

    def send_play(self):
        play_fun = self.vlc_dbus_obj.get_dbus_method('Play', 'org.mpris.MediaPlayer2.Player')
        play_fun()

    def send_pause(self):
        pause_fun = self.vlc_dbus_obj.get_dbus_method('Pause', 'org.mpris.MediaPlayer2.Player')
        pause_fun()

    def send_play_pause(self):
        pp_fun = self.vlc_dbus_obj.get_dbus_method('PlayPause', 'org.mpris.MediaPlayer2.Player')
        pp_fun()

    def send_stop(self):
        stop_fun = self.vlc_dbus_obj.get_dbus_method('Stop', 'org.mpris.MediaPlayer2.Player')
        stop_fun()

    def send_next(self):
        next_fun = self.vlc_dbus_obj.get_dbus_method('Next', 'org.mpris.MediaPlayer2.Player')
        next_fun()

    def send_prev(self):
        prev_fun = self.vlc_dbus_obj.get_dbus_method('Previous', 'org.mpris.MediaPlayer2.Player')
        prev_fun()

    ### other commands just for reference: (use d-feet and move to SessionBus -> org.mpris.MediaPlayer.Player -> Methods)
    #    'Seek'
    #    'OpenUri'
    #    'SetPositon'



if __name__ == '__main__':
    parser = OptionParser(usage='usage: %prog [options] ', version='0.2', description="vlc mediakey remote")  
    parser.add_option('-l', '--play', action='store_true', help='tell vlc to start playback', dest='play', default=False)
    parser.add_option('-t', '--play-pause', action='store_true', help='tell vlc to toggle between play and pause', dest='playpause', default=False)
    parser.add_option('-a', '--pause', action='store_true', help='tell vlc to pause playback', dest='pause', default=False)
    parser.add_option('-s', '--stop', action='store_true', help='tell vlc to stop playback', dest='stop', default=False)
    parser.add_option('-n', '--next', action='store_true', help='tell vlc to play the next track', dest='next', default=False)
    parser.add_option('-p', '--prev', action='store_true', help='tell vlc to play the previous track', dest='previous', default=False)

    (options, args) = parser.parse_args()

    if args=='none':
        parser.print_help()

    vlct = VlcTalker()
    # only run the following commands if the initialization was succesful
    if vlct.vlc_dbus_obj:
        if options.play:
            vlct.send_play()
        elif options.pause:
            vlct.send_pause()
        elif options.playpause:
            vlct.send_play_pause()
            # manual play/pause
            # get current state then call play/pause accordingly
            #state = str(vlct.get_playstate())
            #if state == 'Playing':
            #    vlct.send_pause()
            #else:
            #    vlct.send_play()
        elif options.stop:
            vlct.send_stop()
        elif options.next:
            vlct.send_next()
        elif options.previous:
            vlct.send_prev()
        else:
            parser.print_help()
    else:
        # make sure that the help is printed when there is a problem with the player
        parser.print_help()