/*
Poor Pigs

18 / 18 test cases passed.
Status: Accepted
Runtime: 4 ms
Memory Usage: 5.9 MB
Language: CPP
*/

class Solution {
public:

 int poorPigs(int numBuckets, int timeDie, int timeTest) {
        
        int y = (timeTest/timeDie) + 1,z = (timeTest/timeDie) + 1,count=1;

        if(numBuckets==1) return 0;
        
        while(y<numBuckets){         
            y *= z;
            count++;      
        }
     
        return count;
    }
};