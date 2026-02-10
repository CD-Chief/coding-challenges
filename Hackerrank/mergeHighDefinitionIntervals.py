# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
"""
Solution 1
hold a variaible : currentInterval and a new 2d array
.loop through 2d array. the first interval is copied to the
currentInterval array, if there is another interval you compare it to
current interval, if the ending number of current interval is greater than or equal to
starting of the next interval, replace current interval ending with next intervals ending, if not. Add the current interval to the interval arr and copy the next interval
to current interval and repeat until no more intervals
Edge: no intervals present : return empty array ?
Issue: need to sort intervals first
Issue: Did not consider intervals not being sorted
O(n)"""
#

def mergeHighDefinitionIntervals(intervals):
    newArr = []
    currInterval = None
    
    #handle empty
    if not intervals:
        return newArr
    
    # Sort intervals
    intervals.sort(key=lambda x: x[0])
    
    # i starts from 0
    for i in range(len(intervals)):
        if not currInterval:
            currInterval = intervals[i]
        
        # Last element in array
        if len(intervals) - 1 == i:
            newArr.append(currInterval)
        # Intervals overlap
        elif currInterval[1] >= intervals[i + 1][0]:
            currInterval[1] = max(currInterval[1], intervals[i + 1][1])
        # Intervals don't overlap and clear current
        else:
            newArr.append(currInterval)
            currInterval = intervals[i + 1]
    
    return newArr