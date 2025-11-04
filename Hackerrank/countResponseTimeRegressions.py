# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#
# Solution 1
"""to get the average, in each iteration we add the values to a pool
and divide this pool by how many values we have already passed by and
compare that avg to the current val
edge: responseTimes.length == 0"""

def countResponseTimeRegressions(responseTimes):
    if not len(responseTimes):
        return 0
    
    avgPool = 0
    numsGreater = 0
    
    for i in range(len(responseTimes)):
        if i:
            if responseTimes[i] > (avgPool / float(i)):
                numsGreater += 1
        avgPool += responseTimes[i]
        
    return numsGreater