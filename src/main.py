from model.vlcplayer import VlcPlayer

player = VlcPlayer()

player.play('..\\music\\tracks\\shogeki.mp3')

while True:
    command = input('Enter command: ')
    if command == 'play':
        player.play()
    elif command == 'pause':
        player.pause()
    elif command == 'next':
        player.playNext()
    elif command == 'previous':
        player.playPrevious()
