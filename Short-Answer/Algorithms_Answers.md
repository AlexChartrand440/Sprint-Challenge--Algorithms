#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n). With every increase in the input, the amount of time required will increase at the same rate.
Example: 
5 * 5 * 5 = 125
0 = 0 + 25; 5 passes
10 * 10 * 10 = 1000
0 = 0 + 100; 10 passes


b) Exponential O(c^n). The input drastically changes the speed and effenciency. Doubling the input far more than doubles the amount of time required.
(n = 10) 10 passes * (j * 2 = 5) passes = 50 passes
(n = 20) 20 passes * (j * 10 = 10) passes = 200 pases


c) O(n) The input doubles the speed and effecency.

## Exercise II

    start = 0
    end = len(n)

    while end >= start:
        
        mid = (end + start) // 2;

        if brk(mid):
            if brk(mid - 1):
                end = mid - 1;
            if not brk(mid - 1):
                return mid;
        else not brk(mid):
            if brk(mid + 1):
                return mid + 1;
            else:
                start = mid + 1;
