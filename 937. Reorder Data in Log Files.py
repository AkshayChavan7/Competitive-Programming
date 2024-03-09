class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digLogs = []
        letLogs = []

        for log in logs:
            if log.split(" ")[-1].isdigit(): digLogs.append(log)
            else: letLogs.append(log)
        
        letLogs.sort(key=lambda letters: letters.split(" ")[0])
        letLogs.sort(key=lambda letters: letters.split(" ")[1:])
        return letLogs+digLogs

    # def reorderLogFiles(self, logs: List[str]) -> List[str]:
    #     digLogs = []
    #     letLogs = []

    #     for log in logs:
    #         if log.split(" ")[-1].isdigit():
    #             digLogs.append(log)
    #         else:
    #             splitList = log.split(" ")
    #             letLogs.append([splitList[0], splitList[1:]])
        
        
    #     letLogs.sort(key=lambda letters: letters[0])
    #     letLogs.sort(key=lambda letters: letters[1])
    #     result = []
    #     for letLog in letLogs:
    #         result.append(letLog[0]+" "+" ".join(letLog[1]))
    #     return result+digLogs