# IPv6-Compressor-in-Python
Hello Every One this a small script of IPv6 compresstion
>what can It do?
*compress a 128 bit long IPv6 address to optimum level
ALthough it is a small script but it can comprpess all possible IPv6 adresses
>WHat are the rules for compression?



->Rule 1: Omit Leading 0s

One way to shorten IPv6 addresses is to omit leading 0s in any hextet (that is, 16-bit section). This rule applies only to leading 0s and not to trailing 0s; being able to omit both leading and trailing 0s would cause the address to be ambiguous. Table 4-1 shows a list of preferred IPv6 addresses and how the leading 0s can be removed. The preferred form shows the address using 32 hexadecimal digits.

Table 4-1 Examples of Omitting Leading 0s in a Hextet*
Format	IPv6 Address
Preferred	0000:0000:0000:0000:0000:0000:0000:0000
Leading 0s omitted	   0:   0:   0:   0:   0:   0:   0:   0
or
0:0:0:0:0:0:0:0
Preferred	0000:0000:0000:0000:0000:0000:0000:0001
Leading 0s omitted	   0:   0:   0:   0:   0:   0:   0:   1
or
0:0:0:0:0:0:0:1
Preferred	ff02:0000:0000:0000:0000:0000:0000:0001
Leading 0s omitted	ff02:   0:   0:   0:   0:   0:   0:   1
or
ff02:0:0:0:0:0:0:1
Preferred	fe80: 0000: 0000: 0000:a299:9bff:fe18:50d1
Leading 0s omitted	fe80:   0   :   0:   0:a299:9bff:fe18:50d1
or
fe80:0:0:0:a299:9bff:fe18:50d1
Preferred	2001: 0db8: 1111:000a:00b0:0000:9000:0200
Leading 0s omitted	2001: db8:  1111:   a:  b0:   0:9000: 200
or
2001:db8:1111:a:b0:0:9000:200
Preferred	2001: 0db8: 0000: 0000:abcd:0000:0000:1234
Leading 0s omitted	2001:  db8:    0:    0:abcd:   0:   0:1234
or
2001:db8:0:0:abcd:0:0:1234
Preferred	2001: 0db8: aaaa: 0001:0000:0000:0000:0100
Leading 0s omitted	2001:  db8: aaaa:   1:   0:   0:   0:  100
or
2001:db8:aaaa:1:0:0:0:100
Preferred	2001: 0db8: aaaa: 0001:0000:0000:0000:0200
Leading 0s omitted	2001: db8: aaaa:   1:   0:   0:   0:   200
or
2001:db8:aaaa:1:0:0:0:200
* In this table, the 0s to be omitted are in bold. Spaces are retained so you can better visualize where the 0s were removed.
It is important to remember that only leading 0s can be removed; if you deleted trailing 0s the address would be incorrect. To ensure that there is only one correct interpretation of an address, only leading 0s can be omitted, as shown in the following example:

0s omitted:

2001:db8:100:a:0:bc:abcd:d0b
Incorrect (trailing 0s):

2001:db80:1000:a000:0000:bc00:abcd:d0b0
Correct (leading 0s):

2001:0db8:0100:000a:0000:00bc:abcd:0d0b



->Rule 2: Omit All-0s Hextets

The second rule for shortening IPv6 addresses is that you can use a double colon (::) to represent any single, contiguous string of two or more hextets (16-bit segments) consisting of all 0s. Table 4-2 illustrates the use of the double colon.

Table 4-2 Examples of Omitting a Single Contiguous String of All-0s Hextets*
Format	IPv6 Address
Preferred	0000:0000:0000:0000:0000:0000:0000:0000
(::) All-0s segments	::
Preferred	0000:0000:0000:0000:0000:0000:0000:0001
(::) All-0s segments	::0001
Preferred	ff02:0000:0000:0000:0000:0000:0000:0001
(::) All-0s segments	ff02::0001
Preferred	fe80:0000:0000:0000:a299:9bff:fe18:50d1
(::) All-0s segments	fe80::a299:9bff:fe18:50d1
Preferred	2001:0db8:1111:000a:00b0:0000:0200
(::) All-0s segments	2001:0db8:1111:000a:00b0::0200
Preferred	2001:0db8:0000:0000:abcd:0000:0000:1234
(::) All-0s segments	2001:0db8::abcd:0000:0000:1234
Preferred	2001:0db8:aaaa:0001:0000:0000:0000:0100
(::) All-0s segments	2001:0db8:aaaa:0001::0100
Preferred	2001:0db8:aaaa:0001:0000:0000:0000:0200
(::) All-0s segments	2001:0db8:aaaa:0001::0200
* In this table, the 0s in bold in the preferred address are replaced by the double colon.
Only a single contiguous string of all-0s segments can be represented with a double colon; otherwise, the address would be ambiguous, as shown in this example:

Incorrect address using two double colons:

2001::abcd::1234
Possible ambiguous choices:

2001:0000:0000:0000:0000:abcd:0000:1234
2001:0000:0000:0000:abcd:0000:0000:1234
2001:0000:0000:abcd:0000:0000:0000:1234
2001:0000:abcd:0000:0000:0000:0000:1234
As you can see, if two double colons are used, there are multiple possible interpretations, and you don’t know which address is the correct one.

What happens if you have an address with more than one contiguous string of all-0s hextets—for example, 2001:0db8:0000:0000:abcd:0000:0000:1234? In that case, where should you use the single double colon (::)?

RFC 5952 states that the double colon should represent:

The longest string of all-0s hextets.

If the strings are of equal length, the first string should use the double colon (::) notation.

Therefore, 2001:0db8:0000:0000:abcd:0000:0000:1234 would be written 2001:0db8:: abcd:0000:0000:1234. Applying both Rules 1 and 2, the address would be written 2001:db8::abcd:0:0:1234.

NOTE

Most operating systems, including Cisco IOS and Microsoft Windows, accept the placement of a single double colon (::) in any valid location.

Combining Rule 1 and Rule 2
You can combine the two rules just discussed to reduce an address even further. Table 4-3 illustrates how this works, showing the preferred address, application of rule 1, and application of rule 2. Again, spaces are left so you can better visualize where the 0s have been removed.

Table 4-3 Examples of Applying Both Rule 1 and Rule 2
Format	IPv6 Address
Preferred	0000:0000:0000:0000:0000:0000:0000:0000
Leading 0s omitted	   0:   0:   0:   0:   0:   0:   0:   0
(::) All-0s segments	::
Preferred	0000:0000:0000:0000:0000:0000:0000:0001
Leading 0s omitted	   0:   0:   0:   0:   0:   0:   0:   1
(::) All-0s segments	::1
Preferred	ff02:0000:0000:0000:0000:0000:0000:0001
Leading 0s omitted	ff02:   0:   0:   0:   0:   0:   0:   1
(::) All-0s segments	ff02::1
Preferred	fe80:0000:0000:0000:a299:9bff:fe18:50d1
Leading 0s omitted	fe80:   0:   0:   0:a299:9bff:fe18:50d1
(::) All-0s segments	fe80::a299:9bff:fe18:50d1
Preferred	2001:0db8:1111:000a:00b0:0000:9000:0200
Leading 0s omitted	2001:  db8:1111:  a:  b0:  0:9000:  200
(::) All-0s segments	2001:db8:1111:a:b0::9000:200
Preferred	2001:0db8:0000:0000:abcd:0000:0000:1234
Leading 0s omitted	2001:  db8:  0:   0:abcd:   0:   0:1234
(::) All-0s segments	2001:db8::abcd:0:0:1234
Preferred	2001:0db8:aaaa:0001:0000:0000:0000:0100
Leading 0s omitted	2001:  db8:aaaa:  1:  0:   0:   0:  100
(::) All-0s segments	2001:db8:aaaa:1::100
Preferred	2001:0db8:aaaa:0001:0000:0000:0000:0200
Leading 0s omitted	2001:  db8:aaaa:  1:  0:  0:   0:   200
(::) All-0s segments	2001:db8:aaaa:1::200
Table 4-4 shows the same examples as in Table 4-3, this time showing just the longest preferred form and the final compressed format after implementing both rules.

Table 4-4 IPv6 Address Preferred and Compressed Formats
Preferred Format	Compressed Format
0000:0000:0000:0000:0000:0000:0000:0000	::
0000:0000:0000:0000:0000:0000:0000:0001	::1
ff02:0000:0000:0000:0000:0000:0000:0001	ff02::1
fe80:0000:0000:0000:a299:9bff:fe18:50d1	fe80::a299:9bff:fe18:50d1
2001:0db8:1111:000a:00b0:0000:0000:0200	2001:db8:1111:a:b0::200
2001:0db8:0000:0000:abcd:0000:0000:1234	2001:db8::abcd:0:0:1234
2001:0db8:aaaa:0001:0000:0000:0000:0100	2001:db8:aaaa:1::100
2001:0db8:aaaa:0001:0000:0000:0000:0200	2001:db8:aaaa:1::200
Even after applying the two rules to compress the format, an IPv6 address can still look unwieldy. Don’t worry! Chapter 5, “Global Unicast Address,” shows a technique that I call the 3–1–4 rule. Using that rule makes IPv6 global unicast addresses (GUAs) easier to read than an IPv4 address and helps you recognize the parts of a GUA address. 