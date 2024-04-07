#Write a for loop that takes each number from the numbers list, increments it by 1, and adds it to the result list.
def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    for number in numbers:
        result.append(number + 1)
    
    return result
loop_over_list()