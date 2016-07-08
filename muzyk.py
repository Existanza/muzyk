import subprocess
import os
import random
import time

devnull = open(os.devnull, 'w')
chord_list = ["C", "D", "E", "F", "G", "Am"]


def play_chord(chord):
    path = "./" + chord.lower() + ".sh"
    for _ in range(3):
        subprocess.call(path, stderr=devnull)
    n = next_chord()
    subprocess.call(path, stderr=devnull)
    return n


def next_chord():
    i = random.randrange(len(chord_list))
    print(chord_list[i])
    return chord_list[i]

n = next_chord()
time.sleep(1)
while True:
    n = play_chord(n)
