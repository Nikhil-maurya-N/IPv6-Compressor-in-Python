def validate(s):
    s=s.lower()
    b=bool
    testvar=4
    hex='0123456789abcdef'
    if len(s)==32+7:
        for index,c in enumerate(s):
            # print(index,c,testvar,end=" ")
            if index==testvar and c==':':
                testvar+=5
                b=True
                # print("block1")
            elif c in hex:
                # pass
                # print("block2")
                b=True
            else:
                print(c," in position ",index+1,"is invalid")
                return False
                # print("block3")
        return b
        print(s)        
        # pass
    else:
        print("The length of IPv6 is  not 32+7:",len(s))
        return False

print("Enter a valid IPv6 address!! alike This \nxxxx​:xxxx:​xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")
s=input()
# print(len(s))
print(validate(s))




