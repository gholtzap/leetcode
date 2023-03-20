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