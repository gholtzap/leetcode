function plusOne(digits: number[]): number[] { 
    const isNine = (currentValue) => currentValue == 9
    let special:number[] = [];
    if(digits.every(isNine)){     
        special[0]=1
        for(let i=1;i<digits.length;i++){
            special.push(0)
        }
        special.push(0)
        return special;
    }
    return rec_plus_one(digits,digits.length-1)
};

function rec_plus_one(arr:number[],pos:number):number[]{
        if(arr[pos]==9){
            if(arr.length!=1){
                arr[pos]=0;
            } else {
                arr[pos]=1;
                arr.push(0);
            }
        } else {
            arr[pos]+=1
            return arr;
        }
        return rec_plus_one(arr,pos-1);
    }