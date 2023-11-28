
# Base class for all operating modes. 

class OperatingMode:
    
    # Status for the run
    OK              = 0
    CHANGE_ACTIVE   = 1
    CHANGE_INACTIVE = 2 
    

    def __init__(self):
        
        self.rtc = None
        self.gu = None
        self.display = None
        self.is_active = False 
        
    def set_rtc(self, rtc):
        self.rtc = rtc
        
    def set_unicorn(self, unicorn):
        self.unicorn = unicorn
        
    def set_display(self, display):
        self.display = display
        
    def set_active(self, active):
        self.is_active = active
    
    # This method should be implemented by the operating mode derivation. 
    def run(self):
        return OperatingMode.OK 
