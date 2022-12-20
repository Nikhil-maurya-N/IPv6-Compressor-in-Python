# Here is a script of IPv6 Compression whose rules are assoiciated from https://www.ciscopress.com
print("Enter a valid IPv6 address!! alike This \nxxxx​:xxxx:​xxxx:xxxx:xxxx:xxxx:xxxx:xxxx")
s=input()
lis=s.split(':')
# print(lis)
# for index,ele in enumerate(lis):
#     if ele=="0000":
for index,ele in enumerate(lis):
    if ele.startswith("0000"):
        lis[index]='0'
    elif ele.startswith('000'):
        lis[index]=ele[3:]
    elif ele.startswith('00'):
        lis[index]=ele[2:]
    elif ele.startswith('0'):
        lis[index]=ele[1:]
        # 0sfd:0000:0000:0000:00sf:0000:0000:000d
        # 0000:0000:0000:0000:0000:0000:0000:0001
        
s=":".join(lis)
sub=':0:0:0:0:0:0:0:'
if s[0]=='0':
    s=s[1:]
while(sub not in s):
    sub=sub[2:]
s=s.replace(sub,'::')
# k=s.find(":0")
print("Here is your IPv6 compressed: ")
print(s)