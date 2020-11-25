from typing import List

def checkio(List) -> str:
    
    for i in range(len(List)):
        if List[0][i] == List[1][i] and List[1][i] == List[2][i] and List[0][i] != '.':
            return List[0][i]
        elif List[0][-1] == List[1][-2] and List[0][-1] == List[2][-3] and List[0][-1] != '.':
            return List[0][-1] #diagonal
        elif List[i][0] == List[i][1] and List[i][0] == List[i][2] and List[i][0] != '.':
            return List[i][0]
        elif List[0][0] == List[1][1] and List[0][0] == List[2][2] and List[i][0] != '.':
            return List[0][0] #diagonal
    else:
        return 'D'  