

import java.util.Arrays;

/*
Median of Two Sorted Arrays

2094 / 2094 test cases passed.
Status: Accepted
Runtime: 17 ms
Memory Usage: 50.4 MB
Language: Java
*/


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int size3 = nums1.length+nums2.length;
        double output = 0.0;
        
        int[] nums3 = new int[size3];
        int index = 0;
        
        for(int i = 0; i<nums1.length;i++){
            nums3[i] = nums1[i];
            index++;
        }
     
        
        for(int i = 0; i<nums2.length;i++){
            nums3[i+nums1.length] = nums2[i];
            index++;
        }
        
        Arrays.sort(nums3);
        
        //if even
        if(nums3.length % 2==0){
            int temp = nums3[nums3.length/2];
            temp+=nums3[(nums3.length/2)-1];
            
            output+= (temp/2.0);
        } else {
            output+=nums3[nums3.length/2];
        }
        
        //if odd
        /*
        if(nums3.length % 2==1){
            output+=nums3[nums3.length/2];
        }
        */
        
        return output;
        
    }
}