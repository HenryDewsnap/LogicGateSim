import gateLoader

logging = False




def log(msg):
    if logging == True: print(f"[LGS]: {msg}")



class interpreter:
    def __init__(self, programStr, gates):
        log("Interpreter Object Created.")

        self.memory = {}
        self.programStr = programStr
        self.gates = gateLoader.importGates(gates)
        
        log("Interpreter Object Initialised.")

    #Format: executionData = {"gate":"xor", "inputs":"[0,1]", "outputs":"nameOfOutputVar"}
    def executeGate(self, executionData):
        log(f"EXECUTING: {executionData['gate']} || INPUTS: {executionData['inputs']} || OUTPUTS: {executionData['outputs']}")
        self.memory[executionData['outputs']] = self.gates[executionData["gate"].lower()][str(executionData["inputs"]).replace(" ","")]

    def createVariable(self, variableData):
        log(f"CREATING VARIABLE: {variableData['name']} || STORING: {variableData['value']}")

a = interpreter("", ["xor", "not"])
a.executeGate({"gate":"xor", "inputs":[0,1], "outputs":"var1"})
a.executeGate({"gate":"not", "inputs":a.memory['var1'], "outputs":"var2"})
print(a.memory["var1"])
print(a.memory["var2"])
