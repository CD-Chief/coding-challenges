# [228] Summary Ranges
"""
Solution 1
Loop throught the array, keep var x as the current range, being the first 
number and another var y for previous number and compare y to the next number, 
if the number is +1 of the previous y iterates to that number
this is done until there is no next number or the next number is more than +1
then the range is added to the array [x, y]
edge: empty array is not possible according to description
array with 1 number

struggled with the fact that len gives actual number of elements and 
range gives the numbers with a 0. also had to switch to using range
instead of for num in ...
I also didn't think about handling the last number well
Definetely need to look up better answers
"""
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        def output(start, end): 
            if start == end:
                return str(start)
            else:
                return f"{start}->{end}"
        
        rangeArray = []

        if len(nums) == 1:
            rangeArray.append(output(nums[0],nums[0]))
            return rangeArray
        
        rangeNum = -1
        prevNum = 0
        
        for i in range(len(nums)):
            num = nums[i]
            print(f"now{num} i={i}")
            if i == 0:
                rangeNum = num
                prevNum = num
            else:
                if prevNum +1 == num:
                    prevNum +=1
                    print("next")
                    if i == len(nums) -1:
                        rangeArray.append(output(rangeNum,prevNum))
                else:
                    rangeArray.append(output(rangeNum,prevNum))
                    rangeNum = num
                    prevNum = num
                    print("range")
                    print(rangeArray)
                    if i == len(nums) -1:
                        rangeArray.append(output(rangeNum,prevNum))
        
        return rangeArray