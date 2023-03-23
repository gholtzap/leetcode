class Solution {
public:
    // here we will iterate through every possible power of three until we fin the desired result
    bool isPowerOfThree(int n) {
         return rec(n,1);
    }

    bool rec(int x, long int n){
        // hardcoded for int overload -- problem definition stated it couldn't be a long
        if(x<=0 || n>2147483647)     {return false;}
        else if(x == n)              {return true;}
        else                         {return rec(x,3*n);}
    }
};