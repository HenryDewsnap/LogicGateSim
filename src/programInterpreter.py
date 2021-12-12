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
            varNames = executionData['inputs'].replace(" ","").split(",")
            executionData['inputs'] = list()

            ##For connecting multiple variables.
            for var in varNames:
                for x in self.memory[var]:
                    executionData['inputs'].append(x)



        executionData['inputs'] = str(executionData["inputs"]).replace(" ","")


        log(f"EXECUTING: {executionData['gate']} || INPUTS: {executionData['inputs']} || OUTPUTS: {executionData['outputs']}")
        try:
            self.memory[executionData['outputs']] = self.gates[executionData["gate"].lower()][executionData["inputs"]]
        except:
            exit(f"Failed to execute")


    def createVariable(self, variableData):
        log(f"CREATING VARIABLE: {variableData['name']} || STORING: {variableData['value']}")
        self.memory[variableData['name']] = variableData['value']
        


"""
a = interpreter("", ["xor", "not", "and", "or"])

a.createVariable({"name":"var1", "value":[0]})
a.createVariable({"name":"var44", "value":[1]})
a.executeGate({"gate":"xor", "inputs":"var1", "outputs":"var2"})
a.executeGate({"gate":"not", "inputs":"var2", "outputs":"var3"})


print(a.memory['var1'])
print(a.memory['var2'])
"""
