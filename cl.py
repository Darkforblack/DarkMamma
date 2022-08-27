class palindrome:
    num=123
    revers=0
    while num > 0:
        reminder=num%10
        revers=(revers*10)+reminder
        num=num//10
    print(revers)

#s=palindrome