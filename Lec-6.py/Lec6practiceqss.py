#psq-1
cities = ["pimpri chinchwad", "mumbai", "pune", "noida", "chennai"]
gods = ["shri krishna", "shri vishnu", "shri mahadev", "shri mahalaxmi" ]

def print_len(list):
    print(len(list))


#psq-2
cities = ["pimpri chinchwad", "mumbai", "pune", "noida", "chennai"]
gods = ["shri krishna", "shri vishnu", "shri mahadev", "shri mahalaxmi" ]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")
        
print_list(gods) 

print_list(cities)


#psq-3

def ca_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)




#psq-4

def converter(usd_val):
    int_val = usd_val * 83 
    print(usd_val, "USD =", int_val, "INR")

    converter(1)