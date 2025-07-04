def palindrome(string):
    l=0
    r=len(string)-1
    while l<r:
        if string[l]!=string[r]:
            return False
        l+=1
        r-=1
    return True

def main():
    string="Mississippississim"
    res=palindrome(string.lower())
    print("Is the String Palindrome:",res)

if __name__=="__main__":
    main()

