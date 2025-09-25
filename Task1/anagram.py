# anagrams are 2 words with the same letters in the same frequency

def anagram(a,b):
    a1=a
    b2=b
    a="".join(sorted(a.upper())) #sorting 
    b="".join(sorted(b.upper()))
    if a==b:
        print(f'{a1} and {b2} are anagrams')
    else:
        print(f'{a1} and {b2} are not anagrams')

a=input("Enter a string:")
b=input("Enter second string: ")
anagram(a,b)
print("END")
