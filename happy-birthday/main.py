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



lines = [ 'Happy Birthday To You', 'Happy Birthday To You', 'Happy Birthday Dear ?????', 'Happy Birthday To You' ]

is_a_pressed = False    
is_playing = False

current_line = 0
current_position = 0 

def build_channels(index):
    pass 
    
def reset():
    gu.stop_playing()
    # Configure music channels
    for i in range(len(channels)):
        channels[i].configure(waveforms=Channel.SINE + Channel.SQUARE,
                              attack=0.016,
                              decay=0.168,
                              sustain=0xafff / 65535,
                              release=0.168,
                              volume=10000 / 65535)
    # Reset text positions.
    currentLine = 0
    currentPosition = 0

def clear_screen():
    graphics.set_pen(graphics.create_pen(0,0,0))
    graphics.clear()
    gu.update(graphics) 
    
def text(toDisplay,colour=(255,255,255)):
    clear_screen() 
    graphics.set_pen(graphics.create_pen(colour[0],colour[1],colour[2]))
    graphics.set_font("bitmap8")
    graphics.text(toDisplay,0,1, scale=0.5)
    gu.update(graphics)
    time.sleep(1)
    
beat = 0

def next_beat():
    global beat
    for i in range(len(notes)):
        if notes[i][beat] > 0:
            channels[i].frequency(notes[i][beat])
            channels[i].trigger_attack()
        elif notes[i][beat] == -1:
            channels[i].trigger_release()
    beat = beat + 1
    
    if beat == SONG_LENGTH:
        return False
    
    return True 
    
text("press a")

isPlaying = False

while True:

    if gu.is_pressed(GalacticUnicorn.SWITCH_A):
        if not is_a_pressed:
            reset()
            if ( isPlaying ):
                isPlaying = False
            else:
                text("Happy B'day",colour=(0,255,0))
                isPlaying = True
                
            was_a_pressed = True
        else:
            was_a_pressed = False

    
    
    if isPlaying:

        # Carry on showing the lines and playing the music. 
        is_next = next_beat()
        gu.play_synth()

        if not is_next:
            reset() 
            isPlaying = False
            text("press a")
            
        # if finished all lines, text and music, reset
        # isPlaying = False
        
    time.sleep(0.35) 
