class Solution:

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hori = [1]+hFences+[m]
        verti = [1]+vFences+[n]
        
        s_h=set()
        s_v=set()
        
        for x in hori:
            for y in hori:
                s_h.add(abs(x-y))
        s_h.remove(0)
        
        for x in verti:
            for y in verti:
                s_v.add(abs(x-y))
        s_v.remove(0)
        
        common=s_v.intersection(s_h)
        if len(common)!=0:
            return (max(common)*max(common))%(10**9+7)
        else:
            return -1