'''
https://www.codewars.com/kata/54bb6f887e5a80180900046b
Description:

Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0'''
def longest_palindrome (s):
    length =0
    for x in range( 1,len(s)+1):
        for pos in range(0, len(s) - x+ 1):
            word = s[pos:pos + x]
            if word == word[::-1]:
                length = x
    return length