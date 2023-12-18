# The main.py script that runs at startup on the pico.

from galactic import GalacticUnicorn, Channel
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
import time


gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT


left_hand_notes_1 = (  0, 0, 196, 0, 0, -1, 0, 0, 196, 0, 0, -1,
                       0, 0, 196, 0, 0, -1, 0, 0, 196, 0, 0, -1,
                       0, 0, 262, 0, 0, -1, 0, 0, 262, 0, 0, -1,
                       0, 0, 262, 0, 0, -1, 196, 0, 196, 0, 0, -1)

left_hand_notes_2 = (  0, 0, 165, 0, 0, -1, 0, 0, 175, 0, 0, -1,
                       0, 0, 175, 0, 0, -1, 0, 0, 165, 0, 0, -1,
                       0, 0, 233, 0, 0, -1, 0, 0, 220, 0, 0, -1,
                       0, 0, 196, 0, 0, -1, 175, 0, 165, 0, 0, -1)

left_hand_notes_3 = (  0, 0, 131, 0, 0, -1, 0, 0, 147, 0, 0, -1,
                       0, 0, 123, 0, 0, -1, 0, 0, 131, 0, 0, -1,
                       0, 0, 165, 0, 0, -1, 0, 0, 175, 0, 0, -1,
                       0, 0, 165, 0, 0, -1, 147, 0, 131, 0, 0, -1)

#    147, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 247, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 175, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 330, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 349, 0, 0, 0, 0, 0, 0, 0, 349, 0, 330, 0, 294, 0, 220, 0, 262, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 247, 0, 0, 0, 0, 0, 0, 0, 247, 0, 220, 0, 196, 0, 147, 0, 175, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
#    147, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 247, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 175, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 330, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 349, 0, 0, 0, 0, 0, 0, 0, 349, 0, 330, 0, 294, 0, 220, 0, 262, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 247, 0, 0, 0, 0, 0, 0, 0, 247, 0, 220, 0, 196, 0, 147, 0, 175, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0,
#    147, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 247, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 175, 0, 0, 0, 0, 0, 0, 0, 175, 0, 196, 0, 220, 0, 262, 0, 330, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 349, 0, 0, 0, 0, 0, 0, 0, 349, 0, 330, 0, 294, 0, 220, 0, 262, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 247, 0, 0, 0, 0, 0, 0, 0, 247, 0, 262, 0, 294, 0, 392, 0, 440, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

right_hand_notes = (392, 392, 440, 0, 392, -1, 523, 0, 494, 0, 0, 0,
                    392, 392, 440, 0, 392, -1, 587, 0, 523, 0, 0, 0,
                    392, 392, 784, 0, 660, -1, 523, 0, 494, 0, 440, 0,
                    698, 698, 659, 0, 523, -1, 587, 0, 523, 0, 0, 0)
#    294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 392, 0, 523, 0, 659, 0, 523, 0, 392, 0, 523, 0, 659, 0, 523, 0, 698, 0, 587, 0, 440, 0, 587, 0, 698, 0, 587, 0, 440, 0, 587, 0, 523, 0, 440, 0, 330, 0, 440, 0, 523, 0, 440, 0, 330, 0, 440, 0, 349, 0, 294, 0, 220, 0, 294, 0, 349, 0, 294, 0, 220, 0, 294, 0, 262, 0, 247, 0, 220, 0, 175, 0, 165, 0, 147, 0, 131, 0, 98, 0,
#    294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 392, 0, 523, 0, 659, 0, 523, 0, 392, 0, 523, 0, 659, 0, 523, 0, 698, 0, 587, 0, 440, 0, 587, 0, 698, 0, 587, 0, 440, 0, 587, 0, 523, 0, 440, 0, 330, 0, 440, 0, 523, 0, 440, 0, 330, 0, 440, 0, 349, 0, 294, 0, 220, 0, 294, 0, 349, 0, 294, 0, 220, 0, 294, 0, 262, 0, 247, 0, 220, 0, 175, 0, 165, 0, 147, 0, 131, 0, 98, 0,
#    294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 294, 0, 440, 0, 587, 0, 440, 0, 392, 0, 523, 0, 659, 0, 523, 0, 392, 0, 523, 0, 659, 0, 523, 0, 698, 0, 587, 0, 440, 0, 587, 0, 698, 0, 587, 0, 440, 0, 587, 0, 523, 0, 440, 0, 330, 0, 440, 0, 523, 0, 440, 0, 330, 0, 440, 0, 349, 0, 294, 0, 220, 0, 294, 0, 349, 0, 294, 0, 220, 0, 294, 0, 262, 0, 247, 0, 220, 0, 175, 0, 165, 0, 147, 0, 131, 0, 98, 0)

notes = [left_hand_notes_1, left_hand_notes_2, left_hand_notes_3, right_hand_notes]

SONG_LENGTH = len(right_hand_notes)

# Create 2 channels - one for left hand notes, one for right hand notes.
channels = [gu.synth_channel(i) for i in range(len(notes))]

words = [   (0,'Happy'), (2,'Birthday'), (6,'To'), (8,'You'),
            (12,'Happy'), (14,'Birthday'), (18,'To'), (20,'You'),
            (24,'Happy'), (26,'Birthday'), (30,'Dear'), (32,'?????'),
            (36,'Happy'), (38,'Birthday'), (42,'To'), (44,'You'),
            ]

is_a_pressed = False    
is_playing = False

beat_index = 0
word_index = 0 

def build_channels(index):
    pass 
    
def reset():
    global beat_index,word_index
    beat_index = 0
    word_index = 0
    
    gu.stop_playing()
    # Configure music channels
    for i in range(len(channels)):
        channels[i].configure(waveforms=Channel.SINE + Channel.SQUARE,
                              attack=0.016,
                              decay=0.168,
                              sustain=0xafff / 65535,
                              release=0.168,
                              volume=10000 / 65535)

def clear_screen():
    graphics.set_pen(graphics.create_pen(0,0,0))
    graphics.clear()
    gu.update(graphics) 
    
def text(toDisplay,colour=(255,255,255)):
    clear_screen() 
    graphics.set_pen(graphics.create_pen(colour[0],colour[1],colour[2]))
    graphics.set_font("bitmap8")
    graphics.text(toDisplay,2,1, scale=0.5)
    gu.update(graphics)
    time.sleep(1)
    
def next_beat():
    global beat_index, word_index
    
    for i in range(len(notes)):
        if notes[i][beat_index] > 0:
            channels[i].frequency(notes[i][beat_index])
            channels[i].trigger_attack()
        elif notes[i][beat_index] == -1:
            channels[i].trigger_release()

    beat_index = beat_index + 1
    
    if beat_index == SONG_LENGTH:
        return False
    
    return True 

def next_word():
    global beat_index, word_index
    
    # See if we need to move to the next word. 
    if ( word_index < len(words) ):
        word_beat_index, word = words[word_index]
        print(f'word = {word}, word_beat_index = {word_beat_index}, beat_index = {beat_index}')
        if ( word_beat_index == beat_index ):
            text(word, colour=(0,255,0))
            word_index += 1

text("press a")

next_beat_time = 0

while True:

    if gu.is_pressed(GalacticUnicorn.SWITCH_A):
        if not is_a_pressed:
            reset()
            if ( is_playing ):
                is_playing = False
                gu.stop_playing() 
            else:
                is_playing = True
                next_beat_time = 0 
                
            was_a_pressed = True
        else:
            was_a_pressed = False
    if is_playing:

        #next_word() 

        # Carry on showing the lines and playing the music.
        if ( time.ticks_ms() >= next_beat_time ):
            is_next = next_beat()
            next_beat_time = time.ticks_ms() + 350 
            gu.play_synth()
            if not is_next:
                reset() 
                is_playing = False
                clear_screen(); 
            
        # if finished all lines, text and music, reset
        # isPlaying = False
    time.sleep(0.1) 
