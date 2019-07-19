from operator import itemgetter
import sys

current_key = None
current_value = 0
key = None
value = 0

for line in sys.stdin:
    line = line.strip()
    key,value = line.split('\t')
    value = int(value)

    if current_key == None:
        current_key = key
        current_value = 0   

    if current_key != key:
        print( "{0}\t{1}".format(current_key, current_value) )        
        current_key = key
        current_value = value         
    else:
        current_value += value
    
if current_key == key:
    print( "{0}\t{1}".format(current_key, current_value) )        
       
   



