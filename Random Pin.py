import vlc, random, time, os
os.chdir("C:\\Users\\fraze\\OneDrive\\Old\\Pin Project\\episode_parts")
address = "C:\\Users\\fraze\\OneDrive\\Old\\Pin Project\\episode_parts\\"
print(address)
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

play = 0
theme = vlc.MediaPlayer(address+"Theme.wav")
introSketch = ["1", "2", "3"]
postIntroBanter = ["1", "2", "3"]
sketches = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
banter = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ending = ["1", "2", "3"]

theme.play()
time.sleep(9.63)

whichIntro = introSketch[random.randint(0,1)]
intro = vlc.MediaPlayer(address+"intro_sketch\\"+whichIntro+".wav")
intro.play()
introSketchDuration = duration(address+"intro_sketch\\"+whichIntro+".wav")
time.sleep((decimalise(introSketchDuration)))

whichPostIntro = postIntroBanter[random.randint(0,1)]
postIntro = vlc.MediaPlayer(address+"post_intro\\"+whichPostIntro+".wav")
postIntro.play()
postIntroSketchDuration = duration(address+"post_intro\\"+whichPostIntro+".wav")
time.sleep(decimalise(postIntroSketchDuration))

while play < 3:
    randomSketch = sketches[random.randint(0,7)]
    sketch = vlc.MediaPlayer(address+"sketches\\"+randomSketch+".wav")
    sketch.play()
    sketchDuration = duration(address+"sketches\\"+randomSketch+".wav")
    time.sleep(decimalise(sketchDuration))

    randomBants = banter[random.randint(0,6)]
    bants = vlc.MediaPlayer(address+"banter\\"+randomBants+".wav")
    bants.play()
    bantsDuration = duration(address+"banter\\"+randomBants+".wav")
    time.sleep(decimalise(bantsDuration))

    play = play + 1

whichEnding = ending[random.randint(0,1)]
end = vlc.MediaPlayer(address+"end\\"+whichEnding+".wav")
end.play()
endDuration = duration(address+"end\\"+whichEnding+".wav")
time.sleep(decimalise(endDuration))