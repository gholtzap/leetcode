class Solution {
public:
    int arrangeCoins(int n) {
        return rec(n, 1);
    }

    int rec(int n, int x){
        if(x > n){
            return x-1;
        }

        return rec(n-x,x+1);
    }
};