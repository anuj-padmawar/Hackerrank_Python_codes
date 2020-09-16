# Enter your code here. Read input from STDIN. Print output to STDOUT

def uid_validator(uid):
    characters = list(uid)
    if len(uid) != 10:
        return False

    try:
        first_char=int(characters[0])
    except ValueError:
        pass
    else:
        return False

    digit_count=0
    uppercase_count=0
    for char in characters:
        try:
            if characters.count(char)>1:
                return False
            if int(char) in range(10):
                digit_count+=1
        except ValueError:
            if char.isupper():
                uppercase_count += 1
            continue

    if digit_count < 3 and uppercase_count < 3:
        return False

    return True


if __name__ == "__main__":

    input_no = int(input())
    for i in range(input_no):
        uid = input()
        if uid_validator(uid):
            print("Valid")
        else:
            print("Invalid")
