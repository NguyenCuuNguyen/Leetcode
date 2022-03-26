#Reverse String: prints from index n-1 to 1
result = ""
def reverse_str(idx, new_str):
    global result
    if idx >= 1:
        result += new_str[idx]
        reverse_str(idx-1, new_str[:-1])
    else:
        result += new_str[0] #Base case

def main():
    string = "hello"
    reverse_str(len(string)-1, string)
    print(result)

if __name__ == "__main__":
    main()
