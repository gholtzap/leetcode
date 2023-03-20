function isPowerOfTwo(n: number): boolean {
    return rec_power_of_two(1,n)
};

function rec_power_of_two(x:number,n:number):boolean{
    if(x==n)                {return true} 
    else if(x>2147483648)   {return false}

    return rec_power_of_two(x*2,n)
}