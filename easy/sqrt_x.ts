function mySqrt(x: number):number {
    // here we will iterate through every number and see if num*num is greater our desired result
    // if so, backtrack a bit by returning i-1

    let i = 0
    while((i*i)<=x) {i++}
    return i-1
};