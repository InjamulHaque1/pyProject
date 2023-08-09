print("Hello this is Injamul Haque")
for x in range(1,20,2):
    print(x, end=" ")
print("Hello,I am team member in python lab project and my name is Md Hossain")
a = "Hello World!"
print(a.upper())
print(len(a))

def fun(word):
    newWord = word[::-1]
    if newWord == word:
        print("Palindrome")
    else:
        print("Not palindrome")
fun("racecar")