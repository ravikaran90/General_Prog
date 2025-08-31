import base64

class Solution:
    def b64encoding_decoding(self,string):
        print("Original String:",string)
        
        #Base64 Encoding takes input in Bytes format for Base64 Encode or Base64 Decode
        #Output of Base64 Encode or Base64 Decode is also in Bytes format, which needs to be decoded as well 
        
        #Encoding
        #Bytes Format
        str_bytes=string.encode()
        print("String in Bytes Format:",str_bytes)
        #Base64 Encoded Bytes Format
        b64_bytes=base64.b64encode(str_bytes)
        print("Base64 Bytes Format:",b64_bytes)
        #Base64 
        b64=b64_bytes.decode()
        print("Base64 String:",b64)

        #Decoding
        encoded_bytes=b64.encode()
        #Bytes Format
        print("Base64 Encoded Bytes Format:",encoded_bytes)
        #Decoded
        base64_bytes=base64.b64decode(encoded_bytes)
        print("Base64 Decoded String:",base64_bytes)
        #Decoded String
        print("Final String:",base64_bytes.decode())


def main():
    string="Florida is a beautiful place!"
    obj=Solution()
    obj.b64encoding_decoding(string)

if __name__=="__main__":
    main()