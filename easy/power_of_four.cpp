class Solution {
public:
    // here we will iterate through every possible power of four until we fin the desired result
    bool isPowerOfFour(int n) {
         return rec(n,1);
    }

    bool rec(int x, long int n){
        // hardcoded for int overload -- problem definition stated it couldn't be a long
        if(x<=0 || n>2147483647)     {return false;}
        else if(x == n)              {return true;}
        else                         {return rec(x,4*n);}
    }
};