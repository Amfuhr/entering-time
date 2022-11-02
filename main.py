

def validate():
    hr = 23
    mins = 59
    hours = int(input("enter the value between 0 and 23"))
    minutes = int(input("enter the value between 0 and 59"))
    print(f'you entered {hours} hours and {minutes} minutes')
    while hr < hours:
        print("value out of range!!!")
        hr = int(input("enter hours "))

    while mins < minutes:
        print("value out of range!!! ")
        mins = int(input("enter minutes "))
    return hr, mins

validate()