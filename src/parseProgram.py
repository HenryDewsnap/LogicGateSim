

class parser:
    def __init__(self, program_str, gates):
        self.program_string = program_str.splitlines()
        self.loaded_gates = gates
        self.program_instructions = {}


    def interpret_instruction(self, line):
        pass

    def iterate(self):
        for line in self.program_string:
            pass
