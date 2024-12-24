#A program that calculates the average of a list of numbers.
def cal_avg(num):
    if len(num) == 0:
        return 0  # To handle the case of an empty list
    total= sum(num)
    count = len(num)
    avg= total/count
    return avg

def main():
    count = int(input("Enter the number of elements: "))
    num = []
    print("Enter the numbers:")
    for _ in range(count):
        nums= float(input())
        num.append(nums)
    avg = cal_avg(num)
    print(f"The average of the list is: {avg:.2f}")


main()