import math

num_testcases = int(input())

for i in range(num_testcases):
    testcase = input().split()
    string = testcase[0]
    k = int(testcase[1])
    
    output_string = ""
    
    parts = int(math.ceil(len(string) / k))
    
    if parts >= k:
        valid = True
        for i in range(0, len(string), k):
            if (i + k) >= len(string):
                if len(string[i :]) >= (k - 1):
                    output_string = output_string + string[i :]
                else:
                    valid = False
            else:
                output_string = output_string + string[i : i + k] + "-"
        if valid:
            print(output_string)
        else:
            print(-1)
    
    else:
        print(-1)
    
