class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        greedy_cnt =0 
        left=right=0 
        while len(g)>left and len(s)>right:
            if g[left]<=s[right]:
                greedy_cnt+=1
                left+=1
            right+=1 
            
        return greedy_cnt