    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l = []
        for item in accounts :
            l.append(sum(item))
        return max(l)
        
