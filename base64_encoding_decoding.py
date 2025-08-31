import base64

class Solution:
    def b64encoding_decoding(self,string):
        
        #Encoding
        #Bytes Format
        str_bytes=string.encode()
        print("String in Bytes Format:",str_bytes)
        #base64 Encoded
        b64_bytes=base64.b64encode(str_bytes)
        print("Base64 Bytes Format:",b64_bytes)
        #Base64 
        b64=b64_bytes.decode()
        print("Base64 String:",b64)

        #Decoding
        



def main():
    string="Florida is a beautiful place!"
    obj=Solution()
    res=obj.b64encoding_decoding(string)
    print("Result:",res)

if __name__=="__main__":
    main()