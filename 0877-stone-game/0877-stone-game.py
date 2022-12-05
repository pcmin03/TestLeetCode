class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # bottom up solution dp
        alice, bob = 0, 0
        piles.sort()
        piles = piles[::-1]
        cpiles = piles.copy()
        
        for num,i in enumerate(piles):
            if num %2 == 0 : 
                alice += i
            else: 
                bob += i 

        return True if alice > bob else False