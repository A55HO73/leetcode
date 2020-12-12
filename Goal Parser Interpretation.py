class Solution:
    def interpret(self, command: str) -> str:
        com = command.replace("()", "o").replace("(al)", "al")
        
        return com
