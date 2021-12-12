import gateLoader

logging = True




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
        
        if type(executionData['inputs']) is str:
            try:
                log(f"Reading variable: {executionData['inputs']}")
                executionData['inputs'] = self.memory[executionData['inputs']]
                log(f"Variable Value: {executionData['inputs']}")
            except:
                exit(f"Variable {executionData['inputs']} not found.")
            
        executionData['inputs'] = str(executionData["inputs"]).replace(" ","")
        
        log(f"EXECUTING: {executionData['gate']} || INPUTS: {executionData['inputs']} || OUTPUTS: {executionData['outputs']}")
        self.memory[executionData['outputs']] = self.gates[executionData["gate"].lower()][executionData["inputs"]]

    def createVariable(self, variableData):
        log(f"CREATING VARIABLE: {variableData['name']} || STORING: {variableData['value']}")
