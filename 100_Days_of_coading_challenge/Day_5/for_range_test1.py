target = int(input())

# sum = 0
# for n in range(0, target + 1, 2):  #  target + 1 includes the last num-it adds
#     sum += n
# print(sum)

                            # or

sum = 0
for n  in range(0, target + 1):
    if n % 2 == 0:
     sum += n
print(sum)