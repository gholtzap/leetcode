function isPowerOfTwo(n: number): boolean {
    // here we will iterate through every possible power of two until we fin the desired result
    return rec_power_of_two(1,n)
};

function rec_power_of_two(x:number,n:number):boolean{
    if(x==n)                {return true} 
    // hardcoded for int overload -- problem definition stated it couldn't be a long
    else if(x>2147483648)   {return false}

    return rec_power_of_two(x*2,n)
}