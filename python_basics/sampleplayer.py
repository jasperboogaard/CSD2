import simpleaudio as sa
import time


print("how many tiem?")
numPlaybackTimes = input("")
print(numPlaybackTimes)

print("welk ritme")

#ritme1 = float(ritme)

ritme = [float(x) for x in input().split()]
print(ritme)

ritmelijst = range(0, int(numPlaybackTimes))


for play in ritme:
    wave_obj = sa.WaveObject.from_wave_file("snare.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    time.sleep(play)
    print(play)
    print()
