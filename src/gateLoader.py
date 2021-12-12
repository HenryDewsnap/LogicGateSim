import json

#Copy and pastable TruthTable:
'''
"[0,0]":[],
"[1,0]":[],
"[0,1]":[],
"[1,1]":[]
'''

##Names is a list of the gate titles.
def importGates(names=[]):
    gates = {}
    for name in names:
        try:
            current = json.load(open(f"gates/{name.lower()}.json"))
            gates[current['Name']] = current['TruthTable']
        except:
            print(f"Gate: {name.lower()} not found.")
    
    return gates
