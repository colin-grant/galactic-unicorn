import time

show_debug = True 

def current_time_ms():
    ct_ms = time.ticks_ms()
    return (ct_ms) 

def debug(output_string):
    if ( show_debug ):
        print(output_string)

# draw an icon given a list of colour 'vectors' where each row is defined as a
# series of colours with begin and end columns. 
def draw_icon( display, icon_vectors, x, y, icon_width, icon_height ):
    
    #debug(f'draw_icon: x = {x}, y = {y}, icon_width = {icon_width}, icon_height = {icon_height}')
    #debug(f'draw_icon: icon_vectors = {icon_vectors}, len(icon_vectors) = {len(icon_vectors)}')
    black_pen = display.create_pen(0,0,0)
    display.set_pen(black_pen)
    display.rectangle(x,y,icon_width,icon_height)
    
    if icon_vectors:
        
        for row_num, row_vectors in enumerate(icon_vectors):
            for vector in row_vectors:
                start, length, colour = vector
                pen = display.create_pen(*colour)
                display.set_pen(pen)
                display.line(x+start, y+row_num, x+start+length, y+row_num)