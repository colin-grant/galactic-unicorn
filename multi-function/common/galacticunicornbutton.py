
class GalacticUnicornButton():
    
    def __init__(self, unicorn, button_id):
        
        self.id = button_id
        self.is_currently_pressed = False
        self.unicorn = unicorn
        
    def is_clicked(self):

        is_clicked = False 
        if self.unicorn.is_pressed(self.id):
            if not self.is_currently_pressed: 
                self.is_currently_pressed = True
                is_clicked = True
        else:
            self.is_currently_pressed = False
            
        return is_clicked 
        
    def is_pressed(self):
        
        return self.unicorn.is_pressed(self.id) 
            

        
        
        
        
        
    