def count_substring(string, sub_string):
    start, count = 0, 0
    n = string.find(sub_string)
    while n >= 0:
        count += 1
        start += n+1
        n = string[start:].find(sub_string)
        if n == -1:
            break
    return count


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
