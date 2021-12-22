import gateLoader
import parseProgram

logging = False


def log(msg):
    if logging == True: print(f"[LGS]: {msg}")

class interpreter:
    def __init__(self, programStr, gates):
        log("Interpreter Object Created.")

        self.pointer = 0
        self.memory = {}
        self.programStr = programStr
        self.gates = gateLoader.importGates(gates)

        self.gateNames = []
        self.varFuncIdentifier = "var"
        self.loopFuncIdentifier= "loop"

        for gate in gates:
            self.gateNames.append(gate)

        self.parser = parseProgram.parser(programStr, self.gateNames)

        log("Interpreter Object Initialised.")


    #Format: executionData = {"gate":"xor", "inputs":"[0,1]", "outputs":"nameOfOutputVar"}
    def executeGate(self, executionData):
        if type(executionData['inputs']) is str:
            varNames = executionData['inputs'].replace(" ","").split(",")
            executionData['inputs'] = list()

            ##For connecting multiple variables. (allowing you to use variable names as arguments).
            for var in varNames:
                for x in self.memory[var]:
                    executionData['inputs'].append(x)



        executionData['inputs'] = str(executionData["inputs"]).replace(" ","")


        log(f"EXECUTING: {executionData['gate']} || INPUTS: {executionData['inputs']} || OUTPUTS: {executionData['outputs']}")
        try:
            self.memory[executionData['outputs']] = self.gates[executionData["gate"].lower()][executionData["inputs"]]
        except:
            exit(f"Failed to execute")

    ##Only supports two arguments currently A and B.
    def conditional_goto(self, condition, args, goWhere):
        new_args = {}
        for arg in args:
            if type(arg) is str:
                try: new_args[arg] = self.memory[arg]
                except: exit(f"{arg} not found in memory.")
            else: new_args[str(arg)] = arg
        
        if eval(f"{new_args[args[0]]}{condition}{new_args[args[1]]}") == True:
            self.pointer = goWhere

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
