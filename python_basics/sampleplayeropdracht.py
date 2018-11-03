import simpleaudio as sa
import time

# maak lege lijst aan voor de ritmes
rythmList = []

# vraag de gebruiker hoeveel samples er gespeeld moeten worden
print("How many times do you want to hear the sample??")
numPlaybackTimes = input("")

# sample importeren
wave_obj = sa.WaveObject.from_wave_file("snare.wav")

#vraagt om een ritme
print("Which rythm? You need as much rythms as the amount of samples you've given. (0.25, 0.5, 1)")

# maakt een lijst aan met de ritmes van de input
for rythm in range(0, int(numPlaybackTimes)):
    tijd = input()
    rythmList.append(tijd)
print(rythmList)

# vraagt de gebruiker om een bpm
print("what BPM?")
bpm = input()
aantalSecondesperbeat = 60/int(bpm);
print(aantalSecondesperbeat)

# speelt de samples af uit de lijst met ritme values
for x in rythmList:
    print(x)
    play_obj = wave_obj.play()
    time.sleep(aantalSecondesperbeat * float(x))
