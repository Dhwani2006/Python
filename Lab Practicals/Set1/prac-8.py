#A program that sorts a list of numbers in ascending or descending order.
def sort(nums,order):
    if order == 'asc':
        return sorted(nums)
    elif order=='desc':
        return sorted(nums,reverse=True)
    else:
        return nums

def main():
    count=int(input("\n Enter the elements: "))
    nums=[]
    print("Enter the numbers:")
    for _ in range(count):
        num=float(input())
        nums.append(num)
    order=input("Enter 'asc' for ascending order or 'desc' for descending order: ").lower()

    sorted_nums=sort(nums,order)
    print("The sorted list is: ",sorted_nums)


main()