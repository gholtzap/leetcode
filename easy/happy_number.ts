function isHappy(n: number):boolean {
    if(rec(n,0)== 1){
        return true
    } 
    return false
};

function rec(n:number,count:number):number{
    let charArray:string[] = n.toString().split('')
    let sum:number = 0

    for(let i = 0; i<charArray.length; i++){
        sum+=Math.pow(parseInt(charArray[i]),2)
    }
    
    if(sum==1){return sum} 
    else if(count < 7) {return rec(sum,count+1)} 
    return 0
    
}