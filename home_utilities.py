
def list_matching(matching_info, string, match_from, match_against):
    if string == 'keyMap':
        if matching_info[string] == True:
            x = list()
            y = list()
            for a in match_from.keys():
                if a in match_against:
                    for it in match_from[a].split('/'):
                        if a not in x:
                            x.append(a)
                        if it in match_against and it not in y:
                            y.append(it)
            print(x,y)
            return x,y
        
        
    

def get_keyBindings_dic(key_weight, inputString):
    for item in key_weight.keys():
        keyBindings_dic = {}
        for item in key_weight.keys():
            if item in inputString:
                keyBindings_dic[item] = {
                                        'on' : raw_String_To_List(
                                                key_weight[item]['keyBindingsOn'],
                                                0
                                                ),
                                        'off' : raw_String_To_List(
                                                key_weight[item]['keyBindingsOff'],
                                                0
                                                )
                                        }
    return keyBindings_dic


# tokanaization
def raw_String_To_List(string,ct_bit):
    '''
    input  : string - string need to be pre-processed
             ct_bit - 0 --> splitting string having '-'
                    - 1 --> applying Tokenization
    output : (dictonary) - list of sentences
    '''
    from spacy.lang.en import English
    nlp = English()
    
    if ct_bit == 0:
        return string.split('-')
    elif ct_bit == 1:
        doc = nlp(string)
        temp = dict()
        for item in doc:
            temp[item.i] = item.text
        return temp

           
def match2strings_fuzzy(instring, matchstring):
    from fuzzywuzzy import fuzz
    return fuzz.token_sort_ratio(instring, matchstring) 
    
def Match_Without_Split(string, inString):
    return match2strings_fuzzy(string, inString)



def list_Match_With_replace(string, key, inString):
    for k,v in string.items():
        for x in v:
            cVal = match2strings_fuzzy(x,inString)
            if cVal == 100:
                print(key,k)
                return key, k
            
#----------------------------------------------
                
def accept_string_command():
    # it takes microphone input from user and written string output
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=5) 
        print('sss')
        r.pause_threshold = 0.8
        audio = r.listen(source)

        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    return query

def speak(audio1):
    import pyttsx3 
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio1)
    engine.runAndWait()
    
if __name__ == "__main__":
    pass