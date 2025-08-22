def getLeader(list):
    highest = 0
    highest_sol = list[0]
    for sol in list:
        if sol.rank > highest:
            highest_sol = sol
    return highest_sol

def getSubs(self,list):
    rank = self.rank
    subs = []
    for sol in list:
        if sol.rank < rank:
            subs.append(sol)
    return subs
