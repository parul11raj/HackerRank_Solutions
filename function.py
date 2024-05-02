def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%400==0) and (year%100==0):
        print("True")
    
    return leap

year = int(input())
print(is_leap(year))
