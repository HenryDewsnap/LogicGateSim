import programInterpreter

def main():
    LGSInterpreter = programInterpreter.interpreter("", ["xor", "not", "and", "or"])
    
    LGSInterpreter.createVariable({"name":"var1", "value":[0]})
    LGSInterpreter.createVariable({"name":"var44", "value":[1]})
    LGSInterpreter.executeGate({"gate":"xor", "inputs":"var1,var44", "outputs":"var2"})
    LGSInterpreter.executeGate({"gate":"not", "inputs":"var2", "outputs":"var3"})


    print(LGSInterpreter.memory['var1'])
    print(LGSInterpreter.memory['var2'])

    LGSInterpreter.executeGate({"gate":"not", "inputs":"var44", "outputs":"var44"})

    LGSInterpreter.conditional_goto("==", ["var1", "var44"], 10)
    print(LGSInterpreter.pointer)

if __name__ == "__main__":
    main()
