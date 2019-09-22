import HomeAutomationSource
import home_utilities


def revert(revert_str):
    home_utilities.speak(revert_str)


def perform_operation(ob,op):
    z = 'turning '+op+' the '+ob
    revert(z)
    

def read_object_state(obj):
    return 'on'

def deal_ambiguity(keyMap_conf, ambiguity, keyMap_object, keyMap_operation):
    print(ambiguity)
    if ambiguity['object'] == 0:
        revert('i did not get that! Please say that again')
    
    if ambiguity['object'] == 1 and ambiguity['operation'] == 1:
        perform_operation(keyMap_object[0],keyMap_operation[0])
        return
    if ambiguity['object'] <= 2 and ambiguity['operation'] == 0:
        for obj in keyMap_object:
            c = read_object_state(obj)
            cim = 'do you want me to switch '+c+' the '+obj
            revert(cim)
            string = home_utilities.accept_string_command()
            if 'yes' in string :
                perform_operation(obj,c)
            else:
                if c == 'on':
                    perform_operation(obj,'off')
                elif c == 'off':
                    perform_operation(obj,'on')
        return
            
    elif ambiguity['operation'] == 1 and ambiguity['object'] <= 2:
        for obj in keyMap_object:
            perform_operation(obj,keyMap_operation[0])
        return
    else:
        revert('i can process only two commands at once')

            
            
def perform_keyBindings_match(keyMap_conf, inputString):
    (keyBindings_object2, value_keyBindings_operation2,
         keyBindings_conf2) = HomeAutomationSource.function_keyBindings_words(
                                                         inputString
                                                             )
    if (keyMap_conf + keyBindings_conf2) == 100:
        perform_operation(keyBindings_object2, value_keyBindings_operation2)
    else:
        revert('please say that again')
    
def perform_query_match(keyMap_conf, inputString):    
    (QueryMatching_object, QueryMatching_operation,
                    Query_conf) = HomeAutomationSource.Query_matching(
                                                            inputString
                                                            )
    if Query_conf == 100:
        perform_operation(QueryMatching_object, QueryMatching_operation)
    else:
        perform_keyBindings_match(keyMap_conf, inputString)

def check_ambiguity(inputEntries, inputString):
    ( keyMap_object, keyMap_operation, keyMap_conf,
                         ambiguity ) = HomeAutomationSource.function_keyMap(
                                                             inputEntries
                                                                 )
    
    if keyMap_conf == 40:
        perform_query_match(keyMap_conf, inputString)
    else:
        deal_ambiguity(keyMap_conf, ambiguity, keyMap_object, keyMap_operation)
        
    

        
def accept_command1(inputString):
    print("+++++++++++" ,inputString)

    #Applying tockenaization to input string and stored in dictonary
    input_entries = home_utilities.raw_String_To_List(str(inputString),1) 

    check_ambiguity(input_entries, inputString)
