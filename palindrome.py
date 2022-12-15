word=input().lower()
if word==word[::-1]:
    print(word,"is a palindrome.")
else:
    print(word,"is not a palindrome.")