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
            current = json.load(open(f"gates/{name.lower()}.json", "r"))
            gates[current['Name'].lower()] = current['TruthTable']
        except:
            exit(f"{name.lower()}.json not found.")
    return gates
