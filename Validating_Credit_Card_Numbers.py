# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    num=input()

    x1=bool(re.match(r"^[456]\d{15}$", num))
    x2=bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num=num.replace("-", "")
    x3=bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (x1 or x2) and x3:
        print("Valid")
    else:
        print("Invalid")
