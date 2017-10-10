// There are two sorted arrays nums1 and nums2 of size m and n respectively.

// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

// Example 1:
// nums1 = [1, 3]
// nums2 = [2]

// The median is 2.0
// Example 2:
// nums1 = [1, 2]
// nums2 = [3, 4]

// The median is (2 + 3)/2 = 2.5


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int num1_len = nums1.length;
        int num2_len = nums2.length;
        int res [] = new int[num1_len+num2_len];
        int final_index = (num1_len + num2_len - 1) / 2;
      //  System.out.println("index is " + final_index);
        int j = 0, k = 0;
        for (int i = 0; i <= final_index + 1; i++){
            if (j < num1_len && k < num2_len){
                if (nums1[j] >= nums2[k]){
                    res[i] = nums2[k++];
                }
                else {
                    res[i] = nums1[j++];
                }
                
            }
            else if (j == num1_len && k < num2_len){
        //        System.out.println( "i is "+ i +" k is "+ k);
                res[i] = nums2[k++];
            }
            
            else if (k == num2_len && j < num1_len){
                res[i] = nums1[j++];
            }
            
        }
        
        if ((num1_len + num2_len) % 2 == 0){
         //   System.out.println("res["+ final_index+ "] is "+res[final_index] + " and res[" + (1+final_index)  + "] is " + res[final_index + 1]);
            return (res[final_index] + res[final_index + 1]) / 2.0;
        }else 
            return res[final_index];
    }
}