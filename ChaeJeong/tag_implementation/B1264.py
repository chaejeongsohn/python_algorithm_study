#if문 x in s, x not in s 이용

while True:
    sentence = input()
    if sentence =='#': break
    result =0
    for i in sentence:
        if i in 'aeiouAEIOU': result+=1
    print(result)

    
    
    
