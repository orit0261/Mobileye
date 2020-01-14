S="my.song.mp3 11b" \
  "greatSong.flac 1000b" \
  "not3.txt 5b" \
  "video.mp4 200b" \
  "game.exe 100b" \
  "mov!e.mkv 10000b"

def solution(S):
    music= ('mp3','aac','flac')
    image =('jpg','bmp','gif')
    movie =('mp4','avi','mkv')
    # write your code in Python 3.622
    space1= S.find(" ")
    text = 'Allowed Hello Hollow'
    index = 0
    b_movie=0
    b_music=0
    b_other=0
    b_img=0

    while index < len(S):
       index = S.find(' ', index)
       if index == -1:
           break
       print('space found at', index, S[index-1])
       ext=(S.find('.',index-5,index))
       ext=S[ext+1:ext+5]
       ext=ext.strip()

       sbytes = (S.find('b', index, index + 100))
       sbytes = int(S[index:sbytes])
       print(sbytes)
       if ext in music:
           b_music = b_music + sbytes
       else:
           if ext in movie:
            b_movie = b_movie + sbytes
           else:
            if ext in image:
                b_img = b_img + sbytes
            else:
                b_other = b_other + sbytes
       index += 1 # +2 because len(' ') == 2

    print("music=",b_music)
    print("movie=",b_movie)
    print("image=",b_img)
    print("others=",b_other)


solution(S)