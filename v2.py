import re

import dbus


def disp(name):
    player = dbus.SessionBus().get_object(name, '/org/mpris/MediaPlayer2')
#property_interface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
#for property, value in property_interface.GetAll('org.mpris.MediaPlayer2.Player').items():
#    print(property, ':', value)


    metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata',dbus_interface='org.freedesktop.DBus.Properties')
    for attr, value in metadata.items():
        print(attr, '\t', value)
    print('Artist :\t', metadata['xesam:artist'][0])
    print('Title :\t', metadata['xesam:title'] if 'xesam:title' in metadata else 'Unknown')










bus = dbus.SessionBus()

bus.get_unique_name()






PlayerName=""

for service in bus.list_names():
    if re.match('org.mpris.MediaPlayer2.', service):
            print(service)
            player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')
            property_interface = dbus.Interface(player, dbus_interface='org.freedesktop.DBus.Properties')
            playerState = property_interface.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
            playerpos = property_interface.Get('org.mpris.MediaPlayer2.Player', 'Position')
            print(playerState)
            print(playerpos)
            if playerState=='Playing':
                print("yeh wala")
                PlayerName = service
                disp(PlayerName)




