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
    elif command.startswith('skip'):
        player.skip(int(command.split()[1]))
    elif command.startswith('vol'):
        player.setVolume(int(command.split()[1]))