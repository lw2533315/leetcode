
// Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

// You may assume the integer do not contain any leading zero, except the number 0 itself.

// The digits are stored such that the most significant digit is at the head of the list.
class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        for (int i = digits.length -1  ;i >= 0 ; i--){
            int value = carry + digits[i];
            if (value > 9)
                carry = 1;
            else carry = 0;
            digits[i] = value%10;
        }
        
        if (carry == 1){
            int temp [] = new int[digits.length+1];
            for (int i = 0; i<digits.length; i++){
                temp[i + 1] = temp[i];
            }
            
            temp [0] = carry;
            return temp;
        }
        return digits;
    }
}