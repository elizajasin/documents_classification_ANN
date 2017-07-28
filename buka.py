import re

s = 'my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b'
a = s.split('\n')
music = 0
image = 0
movie = 0
other = 0
for i in range(len(a)):
    tipe = re.search(r'\.(\w+)\s', a[i])
    size = re.search(r'\s(\d+)b', a[i])
    if (tipe.groups()[0] == 'mp3') or (tipe.groups()[0] == 'aac') or (tipe.groups()[0] == 'flac'):
        music = music + int(size.groups()[0])
    elif (tipe.groups()[0] == 'jpg') or (tipe.groups()[0] == 'bmp') or (tipe.groups()[0] == 'gif'):
        image = image + int(size.groups()[0])
    elif (tipe.groups()[0] == 'mp4') or (tipe.groups()[0] == 'avi') or (tipe.groups()[0] == 'mkv'):
        movie = movie + int(size.groups()[0])
    else: other = other + int(size.groups()[0])
print('music '+str(music)+'b\nimages '+str(image)+'b\nmovies '+str(movie)+'b\nother '+str(other)+'b')