def reversal(string):
    l=0
    r=len(string)-1
    string=list(string)
    while l<r:
        string[l],string[r]=string[r],string[l]
        l+=1
        r-=1
    string2="".join(string)
    return string2
    #In-Place
    #reversed_string=string[::-1]# Time Complexity: O(n)
    """
    reversed_string=""
    for char in string:
        #Time Complexity: O(n)
        reversed_string=char+reversed_string
        print(reversed_string)
    print(reversed_string)
    """
    #print(string)
    #while l<r:
    #    string2+=string[r][l]
    #    l+=1
    #    r-=1


def main():
    string="california"
    rev=reversal(string)
    print("Reversed String:",rev)
    #Case Insensitive
    #Removing Spaces
    #Removing Special Characters
    string=string.upper()
  
if __name__=="__main__":
    main()
