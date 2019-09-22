import home_utilities
import os
from recemendingSystem import accept_command1


def main():
    result = home_utilities.accept_string_command()
    if "Ok Google" in result:
        idd="connecting to suvi"
        print(idd)
        home_utilities.speak(idd)
        instring = home_utilities.accept_string_command()
        #print(instring)
        #speak(instring)
        return 1, instring
    else:
        return 0,''
    if "bye" in result:
        home_utilities.speak("Meet you soon")
        exit()
    else:
        home_utilities.speak('Speech not understood')
        main()
            
list1=['light on', 'please switch on the light ', 'switch on light ']
if __name__ == "__main__":
    while 1:
        ijd,inputString = main()
        if ijd == 0:
            break
        else:
            accept_command1(inputString)
        
            