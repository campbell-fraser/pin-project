import vlc, random, time, os
os.chdir("C:\\Users\\fraze\\Documents\\Pin Project")
def duration(source):
    vlcInstance = vlc.Instance()
    player = vlcInstance.media_player_new()
    media = vlcInstance.media_new(source)
    player.set_media(media)
    player.play()
    time.sleep(0.1)
    length = player.get_length()
    player.stop()
    return(length)

def decimalise(number):
    number = str(number)
    last3 = number[(len(number)-3):len(number)]
    durationSeconds = number.replace(last3, "."+last3)
    return(float(durationSeconds))

ending = ["1", "2", "3"]

whichEnding = ending[random.randint(0,2)]
end = vlc.MediaPlayer("C:\\Users\\fraze\\Documents\\Pin Project\\End\\"+whichEnding+".wav")
end.play()
endDuration = duration("C:\\Users\\fraze\\Documents\\Pin Project\\End\\"+whichEnding+".wav")
time.sleep(decimalise(endDuration))