def sort_key(values, group):
    def helper(x):
        if x in group:
            return False
        return True
    # values.sort(key=helper)
    sorted(values, key=helper)


numbers = [8,5,1,2,6,2,4,8,9]
group= {6,8,9}

sort_key(numbers, group)
print(numbers)
# print(sorted(numbers, key=lambda x: x >= 6, reverse = True))
