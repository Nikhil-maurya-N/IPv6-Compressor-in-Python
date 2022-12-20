# Here is a script of IPv6 Compression whose rules are assoiciated from https://www.ciscopress.com
def validate(s):
    s=s.lower()
    b=bool()
    testvar=4
    hex='0123456789abcdef'
    if len(s)==32+7:
        for index,c in enumerate(s):
            if index==testvar and c==':':
                testvar+=5
                b=True
            elif c in hex:
                # pass
                b=True
            else:
                print(c," in position ",index+1,"is invalid")
                return False
        return b
        print(s)        
    else:
        print("The length of IPv6 is  not 32+7:",len(s))
        return False
def compress(s):
    if validate(s):
        
        lis=s.split(':')
        for index,ele in enumerate(lis):
            if ele.startswith("0000"):
                lis[index]='0'
            elif ele.startswith('000'):
                lis[index]=ele[3:]
            elif ele.startswith('00'):
                lis[index]=ele[2:]
            elif ele.startswith('0'):
                lis[index]=ele[1:]
                # 0efd:0000:0000:0000:00ef:0000:0000:000d
                # 0000:0000:0000:0000:0000:0000:0000:0001
                
        s=":".join(lis)
        sub=':0:0:0:0:0:0:0:'
        if s[0]=='0':
            s=s[1:]
        while(sub not in s):
            sub=sub[2:]
        s=s.replace(sub,'::')
        print("Here is your IPv6 compressed: ")
        print(s)
    else:
        print("Hence Entered values is not a valid IPv6")
        
# driver code
print("Enter a valid IPv6 address!! alike This \nxxxx​:xxxx:​xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")
s=input()
compress(s)