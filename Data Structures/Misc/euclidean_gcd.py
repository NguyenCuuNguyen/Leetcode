
def gcd(a, b):
    if a == 0:
        print(f"returning b={b}")
        return b
    print(f"Recursively call gcd({b}%{a}={b%a},{a})")
    return gcd(b%a, a)

# def gcd(a, b):
#     if a == 0: 
#         print(f"returning b={b}")
#         return b
#     print(f"Recursively call gcd({a}%{b}={a%b},{b})")
#     return gcd(a%b, b) #ERROR: Create Infinite loop

# def gcd(a, b):
#     if a == 0: 
#         print(f"returning b={b}")
#         return b
#     print(f"Recursively call gcd({a}%{b}={a%b},{a})")
#     return gcd(a%b, a) #But this works fine

# def gcd(a, b):
#     if b == 0: #ERROR: Create Zero Division error
#         print(f"returning b={b}")
#         return a
#     print(f"Recursively call gcd({b}%{a}={b%a},{a})")
#     return gcd(b%a, a) 

# def gcd(a, b):
#     if a == 0: 
#         print(f"returning b={b}")
#         return b
#     print(f"Recursively call gcd({b}%{a}={b%a},{a})")
#     return gcd(b%a, b) #ERROR: Return wrong answer, verbatim b

if __name__ == "__main__":
    a = 15
    b = 10
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    print("\n")

    a = 35
    b = 10
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
    print("\n")

    a = 31
    b = 2
    print("gcd(", a, ",", b, ") = ", gcd(a, b))