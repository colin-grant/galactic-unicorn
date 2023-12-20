
from common.util import debug

FONT_HEIGHT = 5 
WHITE_RGB = (255,255,255)
BLACK_RGB = (0,0,0)

NUMBERS = [ [1,1,1,
             1,0,1,
             1,0,1,
             1,0,1,
             1,1,1],
            [0,1,0,
             0,1,0,
             0,1,0,
             0,1,0,
             0,1,0],
            [1,1,1,
             0,0,1,
             1,1,1,
             1,0,0,
             1,1,1],
            [1,1,1,
             0,0,1,
             1,1,1,
             0,0,1,
             1,1,1],
            [1,0,1,
             1,0,1,
             1,1,1,
             0,0,1,
             0,0,1],
            [1,1,1,
             1,0,0,
             1,1,1,
             0,0,1,
             1,1,1],
            [1,1,1,
             1,0,0,
             1,1,1,
             1,0,1,
             1,1,1],
            [1,1,1,
             0,0,1,
             0,0,1,
             0,0,1,
             0,0,1],
            [1,1,1,
             1,0,1,
             1,1,1,
             1,0,1,
             1,1,1],
            [1,1,1,
             1,0,1,
             1,1,1,
             0,0,1,
             1,1,1] ]

COLON = [0,
         1,
         0,
         1,
         0]

DEG_C = [1,0,1,1,1,
         0,0,1,0,0,
         0,0,1,0,0,
         0,0,1,0,0,
         0,0,1,1,1 ]


SPACE = [0,0,0,0,0]

DATE_SEP = [0,
            0,
            1,
            0,
            0]

MINUS_SIGN = [0,0,
              0,0,
              1,1,
              0,0,
              0,0]

PCENT_SIGN = [1,0,0,1,
              0,0,1,0,
              0,1,0,0,
              1,0,0,1,
              0,0,0,0] 

# LETTERS USED IN MONTH NAMES
MX_A = [ 1,1,1,
         1,0,1,
         1,1,1,
         1,0,1,
         1,0,1 ]

MX_B = [ 1,1,1,
         1,0,1,
         1,1,0,
         1,0,1,
         1,1,1 ]

MX_C = [ 1,1,1,
         1,0,0,
         1,0,0,
         1,0,0,
         1,1,1 ]

MX_D = [ 1,1,0,
         1,0,1,
         1,0,1,
         1,0,1,
         1,1,0 ]

MX_E = [1,1,1,
     1,0,0,
     1,1,0,
     1,0,0,
     1,1,1 ]

MX_F = [ 1,1,1,
         1,0,0,
         1,1,0,
         1,0,0,
         1,0,0 ]

MX_G = [ 1,1,1,1,
         1,0,0,0,
         1,0,1,1,
         1,0,0,1,
         1,1,1,1 ]

MX_H = [ 1,0,0,1,
         1,0,0,1,
         1,1,1,1,
         1,0,0,1,
         1,0,0,1 ]

MX_I = [ 1,1,1,
         0,1,0,
         0,1,0,
         0,1,0,
         1,1,1 ]

MX_J = [ 1,1,1,
         0,1,0,
         0,1,0,
         0,1,0,
         1,1,0 ]

MX_K = [ 1,0,1,
         1,1,0,
         1,0,0,
         1,1,0,
         1,0,1 ]

MX_L = [ 1,0,0,
         1,0,0,
         1,0,0,
         1,0,0,
         1,1,1 ]

MX_M = [ 1,0,0,0,1,
         1,1,0,1,1,
         1,0,1,0,1,
         1,0,0,0,1,
         1,0,0,0,1 ]

MX_N = [ 1,0,0,1,
         1,1,0,1,
         1,0,1,1,
         1,0,0,1,
         1,0,0,1 ]

MX_O = [ 1,1,1,
         1,0,1,
         1,0,1,
         1,0,1,
         1,1,1 ]

MX_P = [ 1,1,1,
         1,0,1,
         1,1,1,
         1,0,0,
         1,0,0 ]

# Q might need a redesign? 
MX_Q = [ 1,1,1,0,
         1,0,1,0,
         1,1,1,0,
         1,1,1,0,
         0,0,0,1 ]


MX_R = [ 1,1,1,1,
         1,0,0,1,
         1,1,1,1,
         1,0,1,0,
         1,0,0,1 ]

MX_S = [ 1,1,1,
         1,0,0,
         1,1,1,
         0,0,1,
         1,1,1 ]

MX_T = [ 1,1,1,
         0,1,0,
         0,1,0,
         0,1,0,
         0,1,0 ]

MX_U = [ 1,0,1,
         1,0,1,
         1,0,1,
         1,0,1,
         1,1,1 ]

MX_V = [ 1,0,1,
         1,0,1,
         1,0,1,
         1,0,1,
         0,1,0 ]

MX_W = [ 1,0,0,0,1,
         1,0,0,0,1,
         1,0,1,0,1,
         1,1,0,1,1,
         1,0,0,0,1 ]

MX_X = [ 1,0,0,0,1,
         0,1,0,1,0,
         0,0,1,0,0,
         0,1,0,1,0,
         1,0,0,0,1 ]

MX_Y = [ 1,0,1,
         1,0,1,
         1,1,1,
         0,1,0,
         0,1,0 ]

MX_Z = [ 1,1,1,1,1,
         0,0,0,1,0,
         0,0,1,0,0,
         0,1,0,0,0,
         1,1,1,1,1 ]

LETTERS = [ MX_A, MX_B, MX_C, MX_D, MX_E, MX_F, MX_G, 
            MX_H, MX_I, MX_J, MX_K, MX_L, MX_M, MX_N,
            MX_O, MX_P, MX_Q, MX_R, MX_S, MX_T, MX_U,             
            MX_V, MX_W, MX_X, MX_Y, MX_Z ] 
            
MONTH_NAMES = [ [ MX_J, SPACE, MX_A, SPACE, MX_N ],
                [ MX_F, SPACE, MX_E, SPACE, MX_B ],
                [ MX_M, SPACE, MX_A, SPACE, MX_R ],
                [ MX_A, SPACE, MX_P, SPACE, MX_R ],
                [ MX_M, SPACE, MX_A, SPACE, MX_Y ],
                [ MX_J, SPACE, MX_U, SPACE, MX_N ],
                [ MX_J, SPACE, MX_U, SPACE, MX_L ],
                [ MX_A, SPACE, MX_U, SPACE, MX_G ],
                [ MX_S, SPACE, MX_E, SPACE, MX_P ],
                [ MX_O, SPACE, MX_C, SPACE, MX_T ],
                [ MX_N, SPACE, MX_O, SPACE, MX_V ],
                [ MX_D, SPACE, MX_E, SPACE, MX_C ],
                ]


def display_word(display, word, x, y, pen=None, justified='left'):
    
    matrix_list = []
    
    is_first = True 
    for i in range(0,len(word)):
        letter = word[i] 
        if ( letter == ' ' ):
            matrix_list.append(SPACE)
            matrix_list.append(SPACE)
        else:
            if ( letter > 'Z' ):
                letter_index = int(ord(letter) - ord('a'))
            else:
                letter_index = int(ord(letter) - ord('A'))
            
            if ( letter_index >=0 and letter_index < 26 ):
                if ( not is_first ):
                    matrix_list.append(SPACE)
                matrix_list.append(LETTERS[letter_index])
            
        is_first = False
        
    next_x = plot_matrix_list(display, matrix_list, x, y, pen, justified) 

# display time is used to display a 2 digit time separated by a colon.
# this could be hours and minutes (for clock) or minutes and seconds (for timers). 
def display_time(display, figure1, figure2, x, y, pen=None, justified='left'):

    return display_long_time(display, [figure1, figure2], x, y, pen, justified)

# display time with any number of digits. 
def display_long_time(display, figures, x, y, pen=None, justified='left'):
    
    matrix_list = []
    
    is_first = True
    
    for figure in figures:
        if ( not is_first ):
            matrix_list.append(SPACE)
            matrix_list.append(COLON)
            matrix_list.append(SPACE)
            
        figure_matrix = generate_number_matrix_list(figure, min_width=2)
        matrix_list.extend(figure_matrix)
        
        is_first = False 
    
    next_x = plot_matrix_list(display, matrix_list, x, y, pen, justified) 

    return next_x

def display_days(display, days, x, y, pen=None, justified='left'):
    
    #debug(f"display_days, days = {days}, x= {x}, y= {y}")
    
    number_matrix = generate_number_matrix_list(days)
    next_x = plot_matrix_list(display, number_matrix, x, y, pen, justified)
    
    matrix_list = []
    matrix_list.append(SPACE)
    matrix_list.append(MX_D)
    matrix_list.append(MX_A)
    matrix_list.append(MX_Y)
    if ( days != 1 ):
        matrix_list.append(MX_S)
    next_x = plot_matrix_list(display, matrix_list, next_x, y, pen)
    
    return next_x 
    

# TODO - assume an integer for now. 
def display_temp_c(display, temp_c, x, y, pen=None, justified='left'):
    
    # display the number first so that numbers are aligned correctly before the symbol. 
    number_matrix = generate_number_matrix_list(int(temp_c))
    next_x = plot_matrix_list(display, number_matrix, x, y, pen, justified) 

    matrix_list = []
    
    matrix_list.append(SPACE)
    matrix_list.append(DEG_C)
    
    next_x = plot_matrix_list(display, matrix_list, next_x, y, pen) 
    
    return next_x

def display_humidity(display, humidity, x, y, pen=None, justified='left'):

    
    humidity_matrix = generate_number_matrix_list(int(humidity))
    next_x = plot_matrix_list(display, humidity_matrix, x, y, pen, justified) 

    matrix_list = []
    
    matrix_list.append(SPACE)
    matrix_list.append(PCENT_SIGN) 
        
    next_x = plot_matrix_list(display, matrix_list, next_x, y, pen) 
    
    return next_x

def display_date(display, day, month, x, y, pen=None, justified='left'):

    matrix_list = []
    
    day_matrix = generate_number_matrix_list(day, min_width=2)
    month_matrix = generate_number_matrix_list(month, min_width=2)
    
    matrix_list.extend(day_matrix)
    matrix_list.append(SPACE)
    matrix_list.append(DATE_SEP)
    matrix_list.append(SPACE)
    matrix_list.extend(month_matrix) 

    next_x = plot_matrix_list(display, matrix_list, x, y, pen, justified=justified) 
    
    return next_x

# display date in form DD MMM 
def display_long_date(display, day, month, x, y, pen=None, justified='left'):
    
    matrix_list = []
    day_matrix_list = generate_number_matrix_list(day, min_width=2)
    month_matrix_list = MONTH_NAMES[min(12,month)-1]
    
    matrix_list.extend(day_matrix_list)
    matrix_list.append(SPACE)
    matrix_list.append(DATE_SEP)
    matrix_list.append(SPACE)
    matrix_list.extend(month_matrix_list) 

    next_x = plot_matrix_list(display, matrix_list, x, y, pen, justified=justified) 
    
    return next_x


# convert integer number to matrix list 
def generate_number_matrix_list(number, min_width=0):
    
    unit_list = []
    matrix_list = [] 
    
    if ( number < 0 ):
        matrix_list.append(MINUS_SIGN)
        matrix_list.append(SPACE)
        number = abs(number)

    # Extract number digits into a list 
    if ( number > 0 ):
        while number > 0:
            unit = number % 10
            unit_list.insert(0,int(unit))
            number = int(number/10)
    else:
        unit_list = [0] 

    # pad to min width with leading zeros. 
    while len(unit_list) < min_width:
        unit_list.insert(0,0) 

    first = True 
        
    for unit in unit_list:
        # Put a space between each digit (ignoring the 1st, since the caller should already make
        # sure we have space). 
        if not first:
            matrix_list.append(SPACE) 
        else:
            first = False
       
        matrix_list.append(NUMBERS[unit]) 

    return matrix_list 

def get_matrix_list_width(matrix_list):
    
    total_width = 0
    
    for mx in matrix_list:
        mwidth = int(len(mx) / FONT_HEIGHT)
        total_width += mwidth
        
    return total_width 
    
def plot_matrix_list(display, matrix_list, x, y, pen=None, justified='left'):
    
    if ( justified == 'right' ):
        x -= (get_matrix_list_width(matrix_list) - 1)
        if x < 0:
            x = 0 
        
    next_x = x
                           
    for matrix_to_plot in matrix_list:
        next_x = plot_matrix(display, matrix_to_plot, next_x, y, pen)
    
    return next_x 

def plot_matrix(display, matrix, x, y, pen=None):
    
    if pen == None:
        pen = display.create_pen(*WHITE_RGB)
        
    #print(f"plot matrix = {matrix}")
    mwidth = int(len(matrix) / FONT_HEIGHT)
    next_x = x + mwidth
    
    for c in range(0, mwidth):
        for r in range(0,FONT_HEIGHT):
            if ( matrix[r*mwidth + c] == 1 ):
                display.set_pen(pen) 
                display.pixel(x+c, y+r)

    
    return next_x
                           
if __name__ == '__main__' :
    
    print("Inside Main")
    
    import time 
    from galactic import GalacticUnicorn
    from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

    # create galactic object and graphics surface for drawing
    gu = GalacticUnicorn()
    graphics = PicoGraphics(DISPLAY)
    
    gu.set_brightness(0.15)

    pen = graphics.create_pen(255,255,255)
    black_pen = graphics.create_pen(0,0,0) 

    while True:
        for mon in range(1,13):
            
            graphics.set_pen(black_pen)
            graphics.clear()
            print("Displaying date")
            display_long_date(graphics, 1,mon, 52, 0, pen, justified='right')
            display_time(graphics, 14, 45, 52, 6, pen, justified='right')
            display_humidity(graphics, mon, 6, 0, pen, justified='right')
            display_temp_c(graphics, mon - 3, 6, 6, pen, justified='right')
            gu.update(graphics)
            time.sleep(2)
            
    