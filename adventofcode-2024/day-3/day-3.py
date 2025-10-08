import re
sum = 0
def main():
    global sum

    with open("Day 3.txt",'r') as file:
        target_string = file.read().replace('\n','')
    
    target_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    pattern = "mul\(\d\d*\d*,\d\d*\d*\)"
    matches = re.findall(pattern,target_string)
    
    for match in matches:
        s = match.split("(")
        t = s[1].split(")")
        x,y = t[0].split(",")
        sum += int(x)*int(y)

    print(sum)

if __name__ == "__main__":
    main()