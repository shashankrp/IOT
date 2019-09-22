import os
import pandas as pd
path_cwd = os.getcwd()

path_map_file = os.path.join(path_cwd,'map.xlsx')
map_df = pd.read_excel(path_map_file, index_col=0)

'''
query = "SELECT * FROM orders WHERE date_time BETWEEN ? AND ?"
df = pd.read_sql(query, connection,  params=(start_date, end_date))
'''



# creating flag bits for necessory operations
matching_info = {'keyMap' : False,
                 'keyBindingsSentence' : False,
                 'keyBindingsWord' : False,
                 'Query' : False
                    }


key_weight = {}
for item in map_df['keyMap'].tolist():
    key_weight[item] = {
        'iD' : int(map_df[map_df['keyMap'] == item]['iD'].item()),
        
        'weight' : int(map_df[map_df['keyMap'] == item]['weight'].item()),
        
        'keyMapOperation' : \
            str(map_df[map_df['keyMap'] == item]['keyMapOperation'].item()),
        
        'keyBindingsSetBit' : \
            int(map_df[map_df['keyMap'] == item]['keyBindingsSetBit'].item()),
            
        'keySetBindings' : \
            str(map_df[map_df['keyMap'] == item]['keySetBindings'].item()),
        
        'keyBindingsOn' : \
            str(map_df[map_df['keyMap'] == item]['keyBindingsOn'].item()),
            
        'keyBindingsOff' : \
            str(map_df[map_df['keyMap'] == item]['keyBindingsOff'].item()),
            
        'onQuery' : map_df[map_df['keyMap'] == item]['onQuery'].item(),
        
        'offQuery' : map_df[map_df['keyMap'] == item]['offQuery'].item()
        }