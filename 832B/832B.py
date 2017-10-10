pool = input("")
pattern = input("")
number = input("")
number = int(number)
sizeofPattern = len(pattern)
sizeofPool = len(pool)

for i in range(number):
    target = input("")
    yes = True
    sizeofTarget = len(target)
    k = 0
    for j in range(sizeofPattern):
        if pattern[j] == '?':
            if target[k] in pool:
                k += 1
            else:
                print ("NO \n")
                yes = False
                break

        elif pattern[j] == '*':
            loop = sizeofTarget - (sizeofPattern - (j + 1))
            jump = False
            for k in range(k,loop):
                if target[k] in pool:
                    print("NO \n")
                    jump = True
                    yes = False
                   
                    print ("k is in *", k)
                    break
                else:     #不同于forloop在c++里面，k的值不可能达到range的上限，而在c/java里是可以的只是不进入forloop循环
                    k += 1
            if jump:
                break
        else:
            if pattern[j] == target[k]:
                k += 1
            else:
                print ("NO \n")
                yes = False
                break
    if yes and k == sizeofTarget:
        print ("test1")
       
        print ("YES \n")
    if yes and k != sizeofTarget:
        print ("k is ",k)
        print("and sizeofTarget is ",sizeofTarget)
       
        print ("NO \n")
                
