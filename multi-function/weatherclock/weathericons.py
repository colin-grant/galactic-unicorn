
import common.util as util

ORANGE1 = (255,128,0)
ORANGE2 = (255,192,0)
YELLOW = (255,255,0)
WHITE = (255,255,255) 
BLACK = (0,0,0)
BLUE = (70,70,255) 
MIST_GREY = (100,100,100)
GREY = (128,128,128)

ICON_WIDTH = 11 
ICON_HEIGHT = 11

# We draw the icons as an 2d array of lines - each line contains tuples with the start pixel, length and pen colour.
WEATHER_ICONS = { "sunny" : [
                                [],
                                [(1,1,YELLOW), (5,1,YELLOW), (9,1,YELLOW)],
                                [(2,1,ORANGE2), (5,1,ORANGE2), (8,1,ORANGE2)],
                                [(3,1,ORANGE2),(4,3,ORANGE1),(7,1,ORANGE2)],
                                [(3,5,ORANGE1)],
                                [(1,1,YELLOW),(2,1,ORANGE2),(3,5,ORANGE1),(8,1,ORANGE2),(9,1,ORANGE1)],
                                [(3,5,ORANGE1)],
                                [(3,1,ORANGE2),(4,3,ORANGE1),(7,1,ORANGE2)],
                                [(2,1,ORANGE2), (5,1,ORANGE2), (8,1,ORANGE2)],
                                [(1,1,YELLOW), (5,1,YELLOW), (9,1,YELLOW)],
                                [] ],
                  "clear" :  [          [],
                                        [(2,4,GREY)],
                                        [(4,3,GREY),(9,1,WHITE)],
                                        [(5,3,GREY)],
                                        [(1,1,WHITE),(6,2,GREY)],
                                        [(6,2,GREY)],
                                        [(6,2,GREY)],
                                        [(2,1,WHITE),(5,3,GREY)],
                                        [(4,3,GREY)],
                                        [(2,4,GREY),(10,1,WHITE)] ],
                  "cloudy" : [
                                        [],
                                        [(4,3,WHITE)],
                                        [(3,5,WHITE)],
                                        [(1,9,WHITE)],
                                        [(1,9,WHITE)],
                                        [(2,7,WHITE)],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [] ],
                  "overcast" : [
                                        [],
                                        [(4,3,GREY)],
                                        [(3,5,GREY)],
                                        [(1,9,GREY)],
                                        [(1,9,GREY)],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [],
                                        [] ],
                  "rainy" : [
                                        [],
                                        [(4,3,GREY)],
                                        [(3,5,GREY)],
                                        [(1,9,WHITE)],
                                        [(1,9,WHITE)],
                                        [],
                                        [(2,1,BLUE), (4,1,BLUE), (6,1,BLUE), (8,1,BLUE)],
                                        [],
                                        [(3,1,BLUE), (5,1,BLUE), (7,1,BLUE), (9,1,BLUE)],
                                        [],
                                        [] ],
                  "snowy" : [
                                        [],
                                        [(4,3,WHITE)],
                                        [(3,5,WHITE)],
                                        [(1,9,WHITE)],
                                        [(1,9,WHITE)],
                                        [],
                                        [(2,1,WHITE), (4,1,WHITE), (6,1,WHITE), (8,1,WHITE)],
                                        [],
                                        [(3,1,WHITE), (5,1,WHITE), (7,1,WHITE), (9,1,WHITE)],
                                        [],
                                        [] ],
                  "sunny_spells" : [
                                        [],
                                        [(2,3,ORANGE2)],
                                        [(1,5,ORANGE2)],
                                        [(1,4,ORANGE2),(5,2,WHITE)],
                                        [(1,3,ORANGE2),(4,4,WHITE)],
                                        [(2,8,WHITE)],
                                        [(2,8,WHITE)],
                                        [],
                                        [],
                                        [],
                                        [] ],
                  "misty" : [ [],
                              [(0,11,MIST_GREY)],
                              [],
                              [(0,11,MIST_GREY)],
                              [],
                              [(0,11,MIST_GREY)],
                              [],
                              [(0,11,MIST_GREY)],
                              [],
                              [(0,11,MIST_GREY)],
                              [] ]              }


def draw_weather_icon( display, icon_name, x, y ):
    
    icon_vectors = WEATHER_ICONS.get(icon_name)
    util.draw_icon(display, icon_vectors, x, y, ICON_WIDTH, ICON_HEIGHT) 

if __name__ == '__main__' :
    
    print("Inside Main")
    
    import time 
    from galactic import GalacticUnicorn
    from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

    # create galactic object and graphics surface for drawing
    gu = GalacticUnicorn()
    graphics = PicoGraphics(DISPLAY)
    
    gu.set_brightness(0.15)

    while True:
        for icon_name in ["clear","overcast","rainy", "snowy", "cloudy", "sunny_spells", "misty", "sunny" ]:
            
            print(f"Drawing icon {icon_name}")
            draw_weather_icon(graphics, icon_name, 0, 0)
            gu.update(graphics)
            time.sleep(2)
            
    