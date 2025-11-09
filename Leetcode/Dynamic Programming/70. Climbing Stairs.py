# [70] Climbing Stairs
"""
Solution 1 
There will always be at least 1 way to take the stairs, being all single steps
from there we can replace each 2 single steps (if possible) with a double step
and count how many times this is possible. We then double that count excluding
the initial way with single steps as the other way is also possible

To do this in a mathmatical way we can check if the number is odd or even
if its even we can calculate how many double steps you can add
Issue: it actually seems every 3 steps can be turned into a double step
I'm not sure how to mathematically calculate this. I'll just go with brute force 
for now
Edge: ?
Issue: this just does not work

Solution 2
This one was quite difficult to figure out and this probably is not the best way
but after some testing i figured out that the answers outputs foollow a fibonacci
sequence. I know the first 2 outputs, N=1 and N=2 do I can make a loop
to simulate a fib sequence until we reach the N given  """
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        
        # We already know the output for these 2
        if n == 1:
                return 1
        elif n == 2:
                return 2

        # Setup the previous 2 for fib sequence
        prev1 = 2
        prev2 = 1

        sequence = 2
        wayCount = 0

        # Sequence
        while sequence != n:
              sequence += 1
              wayCount = prev1 + prev2

              prev2 = prev1
              prev1 = wayCount
        
        return wayCount