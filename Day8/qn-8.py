given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)
