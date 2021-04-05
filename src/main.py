from model.vlcplayer import VlcPlayer

player = VlcPlayer()

player.play('..\\music\\tracks\\shogeki.mp3')

while True:
    if input() == 'pause':
        player.pause()
    else:
        player.play()