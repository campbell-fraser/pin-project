import vlc, time, os, random
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
    return(durationSeconds)

sketches = ["1", "2", "3", "4", "5", "6", "7", "8"]
randomSketch = str(sketches[random.randint(0,7)])+".wav"
print(randomSketch)

sketchDuration = duration(randomSketch)
print(sketchDuration)

decimalisedDuration = decimalise(sketchDuration)
print(decimalisedDuration)