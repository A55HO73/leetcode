class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        time = []
        lenght = len(keysPressed)
        time.append(releaseTimes[0])
        for i in range(1,lenght):
            time.append(releaseTimes[i] - releaseTimes[i-1])

        mxi = max(time)
        if time.count(mxi) == 1:
            return (keysPressed[time.index(mxi)])
        else :
            t =[]
            for i in  range(lenght):
                if time[i] == mxi:
                    t.append(keysPressed[i])


            return (max(t))       
