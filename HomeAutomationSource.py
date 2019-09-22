import os
import pandas as pd
import numpy as np
import home_utilities
from Home_parameteres import key_weight,map_df,matching_info


def function_keyMap(input_entries):
    '''
    list of keyword and operation present in command
    * resolve ambiguity
    * 10% matching
    '''
    # setting a flag bit for keyMap matching                 
    matching_info['keyMap'] = True
    ambiguity_is = 0
    ambiguity_is = {'object': 0 , 'operation' : 0 }
    keyMatch_dic = dict(zip(map_df['keyMap'].tolist(), map_df['keyMapOperation'].tolist()))
    # performing an keyMap matching operation
    key,op = home_utilities.list_matching(
                        matching_info,
                        'keyMap',
                        keyMatch_dic,
                        list(input_entries.values())
                        )
    c = 40
    if len(op) == 0:
        c = c - 10
    if len(key) > 1 or len(op) > 1:
        c = c - 10
        if len(key) > 1:
            ambiguity_is['object'] = len(key)
        else:
            ambiguity_is['operation'] = len(op) 
    if key == [] and op == []:
        c = 0
    return key, op, c, ambiguity_is


def function_keyBindings_words( inputString):
    '''
    object and operation matching by word by word
    * 60% matching
    '''
    keyBindings_dic = home_utilities.get_keyBindings_dic(
                                                key_weight, inputString
                                                )

    result2,state2 = 0,0
    if len(keyBindings_dic) < 2:
        for x_item in keyBindings_dic.keys():
            for key,val in keyBindings_dic[x_item].items():
                for item in val:
                    for item_y in item.split(' '):
                        if item_y == x_item:
                            continue
                        if item_y in inputString:
                            result2 = x_item
                            state2 = item_y
                            break
                    
    c1 = 60
    if result2 == 0 and state2 == 0:
        c1 = 0
    return result2, state2, c1


def function_keyBindings_sentence(inputString):
    '''
    object and operation matching by sentance
    * 30% matching
    '''
    result1,state1 = 0,0
    keyBindings_dic = home_utilities.get_keyBindings_dic(
                                                key_weight, inputString
                                                )
    for item in key_weight.keys():
        if item in inputString:
            try:
                result1,state1 = home_utilities.list_Match_With_replace(
                                        keyBindings_dic[item], 
                                        item, 
                                        inputString
                                        )
            except:
                pass

    c2 = 30
    if result1 == 0 and state1 == 0:
        c2 = 0
    return result1, state1, c2



# Query matching
def Query_matching(inputString):
    '''
    object and operation matching by whole sentance exactly
    * 100% matching
    '''
    Query_dic = {}
    result3, state3 = 0,0
    for item in key_weight.keys():
        if item in inputString:
            Query_dic[item] = {
                                'onQuery' : \
            home_utilities.raw_String_To_List(key_weight[item]['onQuery'],0),
                                'offQuery' : \
            home_utilities.raw_String_To_List(key_weight[item]['offQuery'],0)
                                }
            keyword = item
    
    for k,v in Query_dic[keyword].items():
        for item in v:
            val = home_utilities.match2strings_fuzzy(inputString, item)
            if val == 100 :
                result3 = keyword
                if  k == 'offQuery':
                    state3 = 'off'
                    break
                elif k == 'onQuery':
                    state3 = 'on'
                    break
                
    c3 = 100
    if result3 == 0 and state3 == 0:
        c3 = 0
    return result3, state3, c3





'''
def accept_command(inputString):
    print("+++++++++++" ,inputString)
    
    
    #Applying tockenaization to input string and stored in dictonary
    input_entries = home_utilities.raw_String_To_List(str(inputString),1) 
    
    (keyMap_object, keyMap_operation, keyMap_conf,
                                    ambiguity) = function_keyMap(
                                                            input_entries
                                                            )
    
    (keyBindings_object1, keyBindings_operation1, keyBindings_conf1,
    keyBindings_object2, value_keyBindings_operation2, 
    keyBindings_conf2) = function_keyBindings(
                                            inputString
                                            )

    QueryMatching_object, QueryMatching_operation, Query_conf = Query_matching(
                                                                inputString
                                                                )

    try:
        if Query_conf == 100:
            return QueryMatching_object, QueryMatching_operation, 0
    except:
        print('jdshgrgkrg-----')
    
    if keyBindings_conf2 + keyMap_conf >= 100:
        if len(keyMap_object) == 1 and len(keyMap_operation) == 1:
            if keyMap_object[0] == keyBindings_object2 and keyMap_operation[0] == value_keyBindings_operation2:
               return keyBindings_object2, value_keyBindings_operation2, 0
    else:
        return '', '',1
          
    try:
        if Query_conf == 100:
            print(QueryMatching_object, QueryMatching_operation, 0)
    except:
        pass
    
    if keyBindings_conf2 + keyMap_conf >= 100:
        if len(keyMap_object) == 1 and len(keyMap_operation) == 1:
            if keyMap_object[0] == keyBindings_object2 and keyMap_operation[0] == value_keyBindings_operation2:
                print( keyBindings_object2, value_keyBindings_operation2, 0)
    else:
        print('', '',1)
   
    
    try:
        print('string match with fuzzywuzzy-40% Match-',keyMap_object,
                                                             keyMap_operation
                                                             )
    except:
        pass
    
    try:
        print('string match with fuzzywuzzy package-30% Match-',
                                          keyBindings_object1,
                                          keyBindings_operation1)
    except:
        pass
    
    
    try:
        print('checking is string present in inputString-95% Match-',
                                                  keyBindings_object2, 
                                                  value_keyBindings_operation2)
    except:
        pass
    
    
    try:
        print('checking exact query matching-100% Match-',QueryMatching_object,QueryMatching_operation)
    except:
        pass
    
    return QueryMatching_object,QueryMatching_operation
    

'''   
    


