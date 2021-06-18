# Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree


def covid(name,body_temp=98):
    print("Name of the patient {}\n Body temperature: {}".format(name,body_temp))

print("Enter patient name")
a=input()
print("Enter Patient body temperature")
b=input()
covid(a,b)
