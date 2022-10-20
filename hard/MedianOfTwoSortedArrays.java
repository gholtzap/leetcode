

import java.util.Arrays;

/*
Median of Two Sorted Arrays

2094 / 2094 test cases passed.
Status: Accepted
Runtime: 15 ms
Memory Usage: 50.4 MB
Language: Java
*/


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
      
        // blank output variable
        double output = 0.0;
        
        // new int array that will is the size of both nums1 and nums2 combined
        int[] nums3 = new int[nums1.length+nums2.length];
        // tracking the index in our new array, so that we can edit the array across different for-loops
        int index = 0;
        
        // iterate through nums1 and add all values to our new array
        for(int i = 0; i<nums1.length;i++){
            nums3[i] = nums1[i];
            index++;
        }
        
        // iterate through nums2 and add all values to our new array
        for(int i = 0; i<nums2.length;i++){
            nums3[i+nums1.length] = nums2[i];
            index++;
        }
        
        // Once we have all values in our new array, we can sort from least to greatest
        Arrays.sort(nums3);
        
        // if the number of values in our new array is even
        if(nums3.length % 2==0){
            int temp = nums3[nums3.length/2];
            temp+=nums3[(nums3.length/2)-1];
            
            output+= (temp/2.0);
        // if the number of values in our new array is odd
        } else {
            output+=nums3[nums3.length/2];
        }
        
        return output;
        
    }
}
