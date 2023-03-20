class Solution {
public:
    bool isPowerOfFour(int n) {
         return rec(n,1);
    }

    bool rec(int x, long int n){
        if(x<=0 || n>2147483647)     {return false;}
        else if(x == n)              {return true;}
        else                         {return rec(x,4*n);}
    }
};