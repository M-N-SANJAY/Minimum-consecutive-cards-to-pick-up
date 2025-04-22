'''
It uses a dictionary d (from collections.defaultdict) to store the last seen index of each card value. 
As it iterates through the list with enumerate, it checks if the current card has been seen before if so, it updates the result res with the smallest distance 
between duplicate cards (calculated as i - d[val] + 1 to include both positions).
It then updates the dictionary with the current index for that card. 
The final result is returned unless no duplicates were found, in which case it returns -1. 
'''
def minimumCardPickup(cards):
        d = defaultdict(list)
        res = float('inf')
        for i, val in enumerate(cards):
            if val in d:
                res = min(res, i - d[val] + 1)
            d[val] = i

        return res if res != float('inf') else -1    
'''
Time Complexity : O(n)
Space Complexity : O(n)
'''
