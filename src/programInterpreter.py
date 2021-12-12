import gateLoader

memory = {}
logging = False

def log(msg):
    if logging == True: print(f"[LGS]: {msg}")

class interpreter:
    def __init__(self, programStr, gates):
        log("Interpreter Object Created.")
        self.programStr = programStr
        self.gates = gateLoader.importGates(gates)
        log("Interpreter Object Initialised.")

    #ExecutionData: {"gate":"xor", "inputs":"[0,1]"}
    def executeGate(self, executionData):
        log(f"EXECUTING: {executionData['gate']} || INPUTS: {executionData['inputs']}")
        return self.gates[executionData["gate"].lower()][executionData["inputs"]]



a = interpreter("xor", ["xor"])
print(a.executeGate({"gate":"xor", "inputs":"[0,1]"}))
