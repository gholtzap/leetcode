# Medium
# Given an array of meeting time intervals consisting of start and end
# times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of 
# conference rooms required.

# Example 1:

# Input:
# [[0, 30],[5, 10],[15, 20]]

# Output:
#  2

# Example 2:

# Input:
#  [[7,10],[2,4]]

# Output:
#  1




def Solution(meetings) -> int:
    output = 1
    print(meetings)
    queue = []
    
    meetings.sort(key = lambda x: x[0])
    
    queue = [meetings[0][1]]
    
    for x in range(1,len(meetings)):
        
    print("sorted",meetings)
    
    
    
    return output


input1 = [[0, 30],[5, 10],[15, 20]]
input2 = [[7,10],[2,4]]

print(Solution(input1))
print(Solution(input2))