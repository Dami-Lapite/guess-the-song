import random
import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory

def prompt(count, playTime, answer):
    if count == 3 :
        prompt_text = input("No more music \n\nType a for answer \n\nType q for quit\n\n")
        if prompt_text == "a":
            print("\n..............................\n")
            print("The correct answer was",answer)
            print("\n..............................\n")
        return True
    else:
        prompt_text = input("Type m for more \n\nType a for answer \n\nType q for quit\n\n")
        if prompt_text == "m":
            pygame.mixer.music.unpause()
            while pygame.mixer.music.get_pos() < playTime:
                continue
            pygame.mixer.music.pause()
            return False
        elif prompt_text == "a":
            print("\n..............................\n")
            print("The correct answer was",answer)
            print("\n..............................\n")
            return True
        else :
            return True

def main():
    pygame.mixer.init()
    root = tk.Tk()
    root.withdraw()

    directory = askdirectory()
    os.chdir(directory)
    list_dir = os.listdir(directory)
    list_dir.sort()


    list_of_songs = []
    for files in list_dir:
        if files.endswith(".mp3"):
            list_of_songs.append(files)
    another_track = True
    score = 0
    while another_track:
        try:
            random_song_index = random.randint(0, len(list_of_songs)-1)

            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load(list_of_songs[random_song_index])
            pygame.mixer.music.play()

            while pygame.mixer.music.get_pos() < 3000:
                continue
            pygame.mixer.music.pause()
            
            done = False
            count = 1
            playTime = 8000
            while not done:
                done = prompt(count, playTime, list_of_songs[int(random_song_index)])
                count += 1
                playTime = 15000
            another_round = input("would you like another round ? (y/n) ")
            if another_round == "n":
                break
        except pygame.error:
            continue

if __name__ == "__main__":
    main()
