class Solution: 
    def binary_search(self,arr,target):
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                right=mid-1
            elif arr[mid]<target:
                left=mid+1
        return left


def main():
    arr=[50,100,120,140,160,180,200,250,400,750,800,1000]
    obj=Solution()
    res=obj.binary_search(arr,120)
    print("Result:",res)

if __name__=="__main__":
    main()