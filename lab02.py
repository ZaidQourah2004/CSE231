n_str = int(input("Input an integer (0 terminates): \n"))
n_int = int(n_str)
odd_count = 0
even_count = 0
positive_int_count = 0
odd_sum = 0
even_sum = 0

# Good stuff goes here



while n_str != 0:
    
    if n_str < 0:
        n_str = int(input("Input an integer (0 terminates): \n"))
        continue
    elif n_str % 2 == 0 and n_str != 0:
        even_count += 1
        even_sum += n_str
        positive_int_count += 1
        n_str = int(input("Input an integer (0 terminates): \n"))
    else:
        odd_count += 1
        odd_sum += n_str
        positive_int_count += 1
        n_str = int(input("Input an integer (0 terminates): \n"))
        




print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
