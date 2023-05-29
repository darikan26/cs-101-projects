# ===============================================================
# CREDITS:
# Code by Derya Arikan and Yifan (Rhyme) Zhou
# Song Title: Merry-Go-Round of Life by Joe Hisaishi
# Sheet Music Rearrangement by rdagnillo on MuseScore
#             https://musescore.com/user/16899726/scores/6601793
# Ghost Choir inspiration by Louie Zong on Youtube
#             https://www.youtube.com/watch?v=kXF3VYYa5TI
# cs101audio library provided by CPSCI-101 Fall '22 instructors
# ===============================================================

from cs101audio import *

choir = Audio()
bass = Audio()

def play_snippet(start, end):
    snippet = Audio()
    snippet = choir[start:end]
    snippet.play()

# ------- 1 -------
Bb4D5 = Audio()
Bb4D5 = generate_music_note('Bb4', 250, 'sine')
Bb4D5.apply_gain(-10)
D5 = Audio()
D5 = generate_music_note('D5', 250, 'sine')
D5.apply_gain(-10)
Bb4D5.overlay(D5)

C5Eb5 = Audio()
C5Eb5 = generate_music_note('C5', 250, 'sine')
C5Eb5.apply_gain(-10)
Eb5 = Audio()
Eb5 = generate_music_note('Eb5', 250, 'sine')
Eb5.apply_gain(-10)
C5Eb5.overlay(Eb5)

for eighth_note in range(0,3):
    choir += Bb4D5 + C5Eb5
    bass += Audio(500)
    
    
# ------- 2 -------
A4C5 = Audio()
A4C5 = generate_music_note('A4', 250, 'sine')
A4C5.apply_gain(-10)
C5 = Audio()
C5 = generate_music_note('C5', 250, 'sine')
C5.apply_gain(-10)
A4C5.overlay(C5)

for eighth_note in range(0,3):
    choir += A4C5 + Bb4D5
    bass += Audio(500)

# ------- 3 -------
G4Bb4 = Audio()
G4Bb4 = generate_music_note('G4', 250, 'sine')
G4Bb4.apply_gain(-10)
Bb4 = Audio()
Bb4 = generate_music_note('Bb4', 250, 'sine')
Bb4.apply_gain(-10)
G4Bb4.overlay(Bb4)

for eighth_note in range(0,3):
    choir += G4Bb4 + A4C5
    bass += Audio(500)
    
# ------- 4 - 5 -------
Fs4A4 = Audio()
Fs4A4 = generate_music_note('Gb4', 175, 'sine')
Fs4A4.apply_gain(-10)
A4 = Audio()
A4 = generate_music_note('A4', 175, 'sine')
A4.apply_gain(-10)
Fs4A4.overlay(A4)

Eb4G4 = Audio()
Eb4G4 = generate_music_note('Eb4', 175, 'sine')
Eb4G4.apply_gain(-10)
G4 = Audio()
G4 = generate_music_note('G4', 175, 'sine')
G4.apply_gain(-10)
Eb4G4.overlay(G4)

D4Fs4 = Audio()
D4Fs4 = generate_music_note('D4', 2250, 'sine')
D4Fs4.apply_gain(-10)
Fs4 = Audio()
Fs4 = generate_music_note('Gb4', 2250, 'sine')
Fs4.apply_gain(-10)
D4Fs4.overlay(Fs4)

D3 = Audio()
D3 = generate_music_note('D3', 250, 'sine')
D3.apply_gain(-10)

A3 = Audio()
A3 = generate_music_note('A3', 250, 'sine')
A3.apply_gain(-10)

D4 = Audio()
D4 = generate_music_note('D4', 500, 'sine')
D4.apply_gain(-10)

choir += Fs4A4 + Eb4G4 + D4Fs4
bass += Audio(1500) + D3 + A3 + D4

# ------- 5 - 6 -------
D4Fs4 = Audio()
D4Fs4 = generate_music_note('D4', 500, 'sine')
D4Fs4.apply_gain(-10)
Fs4 = Audio()
Fs4 = generate_music_note('Gb4', 500, 'sine')
Fs4.apply_gain(-10)
D4Fs4.overlay(A4)

D4 = Audio()
D4 = generate_music_note('D4', 500, 'sine')
D4.apply_gain(-5)

G4 = Audio()
G4 = generate_music_note('G4', 500, 'sine')
G4.apply_gain(-5)

Bb4 = Audio()
Bb4 = generate_music_note('Bb4', 500, 'sine')
Bb4.apply_gain(-5)

choir += D4Fs4 + D4 + G4 + Bb4
bass += Audio(2000)

# ------- 7 -------
G4Bb4D5_half = Audio()
G4Bb4D5_half = generate_music_note('G4', 1000, 'sine')
G4Bb4D5_half.apply_gain(-12)
Bb4 = generate_music_note('Bb4', 1000, 'sine')
Bb4.apply_gain(-12)
D5 = generate_music_note('D5', 1000, 'sine')
D5.apply_gain(-12)
G4Bb4D5_half.overlay(Bb4)
G4Bb4D5_half.overlay(D5)

G4Bb4D5_quarter = Audio()
G4Bb4D5_quarter = generate_music_note('G4', 500, 'sine')
G4Bb4D5_quarter.apply_gain(-12)
Bb4 = generate_music_note('Bb4', 500, 'sine')
Bb4.apply_gain(-12)
D5 = generate_music_note('D5', 500, 'sine')
D5.apply_gain(-12)
G4Bb4D5_quarter.overlay(Bb4)
G4Bb4D5_quarter.overlay(D5)

C3 = Audio()
C3 = generate_music_note('C3', 500, 'sine')
C3.apply_gain(-12)

Bb3 = Audio()
Bb3 = generate_music_note('Bb3', 1000, 'sine')
Bb3.apply_gain(-12)

choir += G4Bb4D5_half + G4Bb4D5_quarter
bass += C3 + Bb3

# ------- 8 -------
C5 = Audio()
C5 = generate_music_note('C5', 500, 'sine')
C5.apply_gain(-10)

Bb4 = generate_music_note('Bb4', 500, 'sine')
Bb4.apply_gain(-10)

A4 = Audio()
A4 = generate_music_note('A4', 500, 'sine')
A4.apply_gain(-10)

D3 = Audio()
D3 = generate_music_note('D3', 500, 'sine')
D3.apply_gain(-10)

C4 = Audio()
C4 = generate_music_note('C4', 1000, 'sine')
C4.apply_gain(-10)

choir += C5 + Bb4 + A4
bass += D3 + C4

# ------- 9-10 -------

Bb4_ext = generate_music_note('Bb4', 2250, 'sine')
Bb4_ext.apply_gain(-10)

G4 = generate_music_note('G4', 250, 'sine')
G4.apply_gain(-10)

Bb4_eighth = generate_music_note('Bb4', 250, 'sine')
Bb4_eighth.apply_gain(-10)

D5 = generate_music_note('D5', 250, 'sine')
D5.apply_gain(-10)

G3 = Audio()
G3 = generate_music_note('G3', 500, 'sine')
G3.apply_gain(-10)

Bb3 = generate_music_note('Bb3', 1000, 'sine')
Bb3.apply_gain(-10)

D4 = generate_music_note('D4', 1000, 'sine')
D4.apply_gain(-10)

choir += Bb4_ext + G4 + Bb4_eighth + D5
bass += G3 + Bb3 + G3 + D4

# ------- 11 -------
G5_half = Audio()
G5_half = generate_music_note('G5', 1000, 'sine')
G5_half.apply_gain(-10)

G5 = Audio()
G5 = generate_music_note('G5', 500, 'sine')
G5.apply_gain(-10)

D4 = generate_music_note('D4', 1000, 'sine')
D4.apply_gain(-10)
 
C3 = generate_music_note('C3', 500, 'sine')
C3.apply_gain(-10)

choir += G5_half + G5
bass += C3 + Bb3

# ------- 12 -------

F5 = Audio()
F5 = generate_music_note('F5', 500, 'sine')
F5.apply_gain(-10)

Eb5 = Audio()
Eb5 = generate_music_note('Eb5', 500, 'sine')
Eb5.apply_gain(-10)

F3 = Audio()
F3 = generate_music_note('F3', 500, 'sine')
F3.apply_gain(-10)

choir += G5 + F5 + Eb5
bass += F3 + C4

# ------- 13-14 -------
F5_ext = generate_music_note('F5', 2250, 'sine')
F5_ext.apply_gain(-10)

A4D5 = generate_music_note('A4', 750, 'sine')
A4D5.apply_gain(-12)
D5 = generate_music_note('D5', 750, 'sine')
D5.apply_gain(-12)
A4D5.overlay(D5)

F5_ext.overlay(Audio(1500) + A4D5)

A4 = generate_music_note('A4', 250, 'sine')
A4.apply_gain(-12)

D5 = generate_music_note('D5', 250, 'sine')
D5.apply_gain(-12)

F5_eighth = Audio()
F5_eighth = generate_music_note('F5', 250, 'sine')
F5_eighth.apply_gain(-12)

Bb3 = generate_music_note('Bb3', 500, 'sine')
Bb3.apply_gain(-10)

A3D4 = Audio()
A3D4 = generate_music_note('D4', 1000, 'sine')
A3D4.apply_gain(-13)
D4 = generate_music_note('D4', 1000, 'sine')
D4.apply_gain(-13)
A3D4.overlay(D4)


choir += F5_ext + A4 + D5 + F5_eighth
bass += Bb3 + D4 + F3 + A3D4 

# ------- 15 -------
A5 = Audio()
A5 = generate_music_note('A5', 1000, 'sine')
A5.apply_gain(-10)

Bb3 = generate_music_note('Bb3', 1000, 'sine')
Bb3.apply_gain(-10)

E3 = Audio()
E3 = generate_music_note('E3', 500, 'sine')
E3.apply_gain(-10)

choir += A5 + G5
bass += E3 + Bb3

# ------- 16 -------
E5 = Audio()
E5 = generate_music_note('E5', 500, 'sine')
E5.apply_gain(-10)

A3 = generate_music_note('A3', 500, 'sine')
A3.apply_gain(-10)

Cs4 = Audio()
Cs4 = generate_music_note('Db4', 1000, 'sine')
Cs4.apply_gain(-10)

choir += F5 + E5 + F5
bass += A3 + Cs4

# ------- 17 -------
A3 = generate_music_note('A3', 1000, 'sine')
A3.apply_gain(-10)

choir += G5_half + F5
bass += D3 + A3

# ------- 18 -------
E5 = generate_music_note('E5', 1000, 'sine')
E5.apply_gain(-10)

D5 = generate_music_note('D5', 500, 'sine')
D5.apply_gain(-10)

F3 = generate_music_note('F3', 1000, 'sine')
F3.apply_gain(-10)

choir += E5 + D5
bass += C3 + F3

# ------- 19 -------
Bb2 = generate_music_note('Bb2', 500, 'sine')
Bb2.apply_gain(-10)

choir += C5 + Bb4 + C5
bass += Bb2 + F3
# ------- 20 -------
G4 = generate_music_note('G4', 500, 'sine')
G4.apply_gain(-10)

A2 = Audio()
A2 = generate_music_note('A2', 500, 'sine')
A2.apply_gain(-10)

E3 = generate_music_note('E3', 1000, 'sine')
E3.apply_gain(-10)

choir += D5 + C5 + G4
bass += A2 + E3
# ------- 21 -------
A4_ext = generate_music_note('A4', 1500, 'sine')
A4_ext.apply_gain(-10)

D4 = generate_music_note('D4', 250, 'sine')
D4.apply_gain(-10)
G4 = generate_music_note('G4', 250, 'sine')
G4.apply_gain(-10)
A4 = generate_music_note('A4', 250, 'sine')
A4.apply_gain(-10)

A4_ext.overlay(Audio(750) + D4 + G4 + A4)

G3 = generate_music_note('G3', 1000, 'sine')
G3.apply_gain(-10)

choir += A4_ext 
bass += D3 + G3

# ------- 22 -------
D5A4 = Audio()
D5A4 = generate_music_note('D5', 1500, 'sine')
D5A4.apply_gain(-12)
A4 = generate_music_note('A4', 1500, 'sine')
A4.apply_gain(-12)
D5A4.overlay(A4)

D3G3 = Audio()
D3G3 = generate_music_note('D3', 1500, 'sine')
D3G3.apply_gain(-12)
G3 = generate_music_note('G3', 1500, 'sine')
G3.apply_gain(-12)
D3G3.overlay(G3)

choir += D5A4
bass += D3G3

# ------- END OF THE SHEET MUSIC EXCERPT -------
choir.overlay(bass)
print(len(choir))

# ------- A LITTLE GHOST STORY -------

choice1 = input("A mysterious ghost has appeared!\nWhat do you do?\n A. Freak out and run away\n B. Gently approach the ghost and say hello\n C. Skip the story and let me listen to the full song, please!\n")
if choice1 == "A":
    print("The ghost disappears back into where it came from and seems upset.\n Try again tomorrow night, maybe you'll be less scared then!")
elif choice1 == "C":
    choir.play()
elif choice1 == "B":
    choice2 = input("You: Hello? \nGhost: Hello! Would you like me to sing for you?\n A. Yes, of course!\n B. No, go away!\n")
    if choice2 == "B":
        print("The ghost is upset that you don't want to hear her friends sing, and leaves.")
    elif choice2 == "A":
        print("Two other ghosts materialize, and the trio begins to sing.")
        play_snippet(0,7100)
        choice3 = input("The ghosts look at you to see your reaction. How do you react?\n A. You are gaping in astonishment. The ghosts are so cute and talented!\n B. You are not impressed. You are practically oozing boredom.\n")
        if choice3 == "B":
            print("The ghosts are sad that you don't like their choir, and they leave.")
        elif choice3 == "A":
            print("The ghosts are happy to see that you are impressed, and continue singing.")
            play_snippet(7100,len(choir))
            print("The ghosts gently finish off the melody.\n Ghosts: Thank you for listening to our choir!\n Ghosts: Good night!")
            