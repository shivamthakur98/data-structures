def towerOfHanoi(source, helper, dest, n):
    if n == 0:
        return
    if n == 1:
        print(source, dest)

    towerOfHanoi(source, dest, helper, n-1)
    print(source, dest)
    towerOfHanoi(helper, source, dest, n-1)

print("Enter source, helper, destination and no. of disks")
source, helper, destination, disk = [el for el in input().strip().split(" ")]
towerOfHanoi(source, helper, destination, int(disk))
