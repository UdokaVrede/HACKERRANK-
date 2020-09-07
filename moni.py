#swapcase of characters
def swap_case(s):
    word=''
    for i in range(len(s)):
        if s[i].isupper():
            word+=s[i].lower()
        elif s[i].islower():
            word+=(s[i]).upper()
        else:
            word+=s[i]
    return word

print(swap_case('HackerRank.com presents "Pythonist 2".'))

#spliting sentences and joining with a new character
def split_and_join(line):
    # write your code here
    word=line.split(" ")
    new_line="-".join(word)
    return new_line

print(split_and_join("Raphael was sick yesterday but He is fine now, that's my stubborn boyfriend"))

#add names
def print_full_name(a, b):
    print("Hello " + a + ' ' + b + '!'+" You just delved into python.")

print(print_full_name('Ross', 'Taylor'))

#count re-occurring sub strings in string
def count_substring(string, sub_string):
    v=len(sub_string)
    count=0
    for i in range(len(string)):
        
        if (string[i:v])== sub_string:
            print(string[i:v])
            count+=1 
        v+=1
    return count

print(count_substring('ABCDCDC','CDC'))

# sette = 'qA2'
# for S in sette:
#     print(S)
#     if S.isalnum() or (S.isalpha() or S.isnum()) or (S.isupper() or S.islower()):
#         print('Truetre')
#     if sette.isalnum() or (sette.isalpha() or sette.isnum()) or (sette.isupper() or sette.islower()):
#         print('True')
#     else:
#         print('False')

print('=============================================================')
str = input()
print (any(c.isalnum()  for c in str))
print (any(c.isalpha() for c in str))
print (any(c.isdigit() for c in str))
print (any(c.islower() for c in str))
print (any(c.isupper() for c in str))


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



import textwrap 

value = """This function wraps the input paragraph such that each line 
in the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""

# Wrap this text. 
wrapper = textwrap.TextWrapper(width=5) 

word_list = wrapper.wrap(text=value) 

# Print each line. 
for element in word_list: 
	print(element) 

word=textwrap.TextWrapper(width=12).wrap(text=value)
print(words for words in word)



if __name__ == '__main__':
        N, M = map(int, input().split(" "))

        for i in range(N):
                pattern = ".|."
                if i < (N-1)/2:
                        print((pattern * (2*i+1)).center(M, "-"))
                elif i == (N-1)/2:
                        print("WELCOME".center(M, "-"))
                else:
                        print((pattern * (2*(N-1-i)+1)).center(M, "-"))
                        print(i)