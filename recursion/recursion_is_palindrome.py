def reverse_string(string,index):
    if len(string)==index:
        try:
            return string[index]
        except IndexError:
            return ''
    return reverse_string(string,index+1)+string[index]

def is_palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            substring=string[1:-1]
            return is_palindrome(substring)
        return False

print(is_palindrome("Udacity"))
print(is_palindrome("madam"))
print(is_palindrome("abba"))
print(is_palindrome("a"))
# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")

