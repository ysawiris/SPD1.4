"""
    Remove Duplicates from Sorted List
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    Example 1:

    Input: 1->1->2
    Output: 1->2
    Example 2:

    Input: 1->1->2->3->3
    Output: 1->2->3

    Recursion function to remove duplicates from a sorted array in O(n)
"""
def removeDuplicates(nums, index=0, length=0, count=0):
    """
    Variable Table:
        Uncomment the print statements below
        to view the variable table in the terminal 
    """
    # print("count:", count)
    # print("nums: ", nums)
    # print('length: ', length)
    if count == 0:
        length = len(nums) - 1 
        
    if count + 1 == length:
        return nums

    if nums[index] != nums[index + 1]:
        removeDuplicates(nums, index + 1, length, count + 1)

    

if __name__ == "__main__":
    nums = [0,0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,4,5,6,6,7]

    list = removeDuplicates(nums)
    print(list)
