class Solution {
    public static String multiply(String num1, String num2) {
       int size_n1 = num1.length();
       int size_n2 = num2.length();
	   
	   //任何为0的string 返回0
        if (num1.charAt(0) == '0' || num2.charAt(0) == '0')
            return "0";
       
       //需要修改固定位置的字符所以用StringBuffer
        StringBuffer product = new StringBuffer("");
		
		//填充‘0’
	   for ( int i = 0 ; i< size_n1 + size_n2; i++)
		   product.append('0');
	   
	   
        for(int i = size_n1 -1 ; i>=0; i--){  //num2
            int carry = 0;

            
            for(int j = size_n2 - 1; j>=0; j--){  //num1
                //当前的index
				int index = j + i + 1;
                int value = product.charAt(index)-'0' + (num1.charAt(i) - '0' ) * (num2.charAt(j) - '0') + carry;
                carry = value/10;
                product.setCharAt(index, (char)(value%10 + '0'));



            }
			//当要用新的乘数位时进位要处理
            product.setCharAt(i,(char)(carry+'0'));
        }
		
		//把product里面开头的0都去掉
         String temp = "";
        System.out.println("size of product is "+ product.toString());
        for (int i = 0; i< size_n1 + size_n2; i++){
            if (product.charAt(i) != '0'){
                System.out.println("the index is "+ i);
                temp = product.substring(i);   //StringBuffer.substring()返回的是String
				//所以要 申请一个临时的
                break;
            }
        }
		return temp;
    }
}