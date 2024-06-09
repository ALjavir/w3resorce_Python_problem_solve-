#pro3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
#[10,20,30,40,50,60,70,80,90]
def cab(int_n):
    k = 3-1
    h = 0
    g = (len(int_n))
    while g>0:
        h = (h+k)%g
        print(int_n.pop(h))
        g-=1
cab([10,20,30,40,50,60,70,80,90])        