
show_debug = True 

def current_time_ms():
    ct_ms = time.ticks_ms()
    return (ct_ms) 

def debug(output_string):
    if ( show_debug ):
        print(output_string) 