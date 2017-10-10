/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javatest;

import java.util.Scanner;

/**
 *
 * @author olive
 */
public class Javatest {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String pool;
		String pattern;
		int number;
		String target;
		Scanner input = new Scanner(System.in);

		pool = input.next();
		pattern = input.next();
		number = input.nextInt();

		int sizeofPattern = pattern.length();
		int sizeofPool = pool.length();

		for( int i = 0; i < number; i++) {
			target = input.next();
			Boolean yes = true;
			int sizeofTarget = target.length();
			int k = 0;

			for (int j = 0; j < sizeofTarget; j++) {
				if (pattern.charAt(j) == '?') {
					if (pool.indexOf(target.charAt(k)) != -1) {
						k++;
					} else {
						System.out.println("NO");
						yes = false;
						break;
					}
				}else if (pattern.charAt(j) == '*') {
					int loop = sizeofTarget - (sizeofPattern - (j + 1));
					Boolean jump = false;
					for (; k < loop; k++) {
						if(pool.indexOf(target.charAt(k)) != -1){
							System.out.println("NO");
							jump = true;
							yes = false;
							break;
						}
					}
					if (jump) break;
				}else {
					if (pattern.charAt(j) == target.charAt(k))
						k++;
					else {
						System.out.println("No");
						yes = false;
						break;
					}
				}
			}
			if (yes && k == sizeofTarget)
				System.out.println("YES");
			if (yes && k != sizeofTarget)
				System.out.println("NO");
		}

    }
    
}
