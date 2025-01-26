def mean_Of_Group(a, b, c, d, e):
    return (a + b + c + d + e) / 5

def median_Of_Group(a, b, c, d, e):
    nums = [a, b, c, d, e]
    nums.sort()
    index = 2
    return (nums[index])

def results():
    if choice == 'mean':
        print('Your result is:')
        print(mean_Of_Group(a, b, c, d, e))
    elif choice == 'median':
        print('Your result is:')  
        print(median_Of_Group(a, b, c, d, e))
    else:
        return

def results2():
    if choice == 'mean':
        print('Your result is:')
        print(mean_Of_Group(a, b, c, d, e))
    elif choice == 'median':
        print('Your result is:')  
        print(median_Of_Group(a, b, c, d, e))
    else:
        print('It seems like you are not even trying, goodbye!1')
    

print('Please enter 5 numbers:')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

choice = 0

print('Please choose either mean or median as your result:')
choice = str(input())
results()

print('Really? How did you mess that up? Choose again:')
choice = str(input())
results2()

