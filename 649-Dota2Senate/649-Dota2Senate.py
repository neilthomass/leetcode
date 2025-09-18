# Last updated: 9/17/2025, 6:08:10 PM

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r = deque()
        d = deque()

        for i, v in enumerate(senate):
            if v == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            ri = r.popleft()
            di = d.popleft()

            if ri < di:
                r.append(ri + len(senate))
            else:
                d.append(di + len(senate))


        return "Radiant" if r else "Dire"