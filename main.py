# Imports
import datetime
import scheduleAPI


# Global Variables


# Public Functions
    
    
def main():
    schedule = read_schedule('schedule')
    
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if timing_exists(current_time, schedule):
            # display certain emotion or movement
            pass
                
        else:
            # display random emotions or movements
            pass

        
if __name__ == "__main__":
    #main()
	pass
    