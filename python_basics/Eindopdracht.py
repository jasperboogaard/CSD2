import simpleaudio as sa
import time
import random

samples = [sa.WaveObject.from_wave_file("snare.wav"), sa.WaveObject.from_wave_file("hat.wav"),sa.WaveObject.from_wave_file("tom.wav") ]
#de samples worden gedefinieerd: sample snare is 0, sample hat is 1, sample tom is 2

#we vragen welke maatsoort en welk bpm er gebruikt moet worden, en die worden gedefinieerd
print("wil je maatsoort 3/4 of 5/4?")
rythmChoice = input()

print("welk bpm wil je?")
bpm = int(input())

print("je hebt gekozen voor het bpm", bpm, "en de maatsoort", rythmChoice)

# calculate the duration of a quarter note
quarterNoteDuration = 60 / bpm
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

# create a list to hold the timestamps
timestamps = [0.25, 0.5, 0.25, 0.5, 0.5, 1, 1]

print(timestamps)
#nu maken we een functie die de durations omzet naar timestamps16th
lijst2 = [0]

item = 0

for duration in timestamps:
    timestamp = duration * 4
    final = lijst2[item] + timestamp
    lijst2.append(final)
    item = item + 1

print(lijst2)

#nu maken we de samplelijst
sampleList = []

for timestamp in timestamps:
    sampleList.append(random.randrange(0, 3, 1))

print(sampleList)

#nu gaan we de samplelijst afspelen

for x in sampleList:
    samples[x].play()
    time.sleep(0.1)
