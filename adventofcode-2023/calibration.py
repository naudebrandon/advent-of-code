sum = 0
word_list = []

with open('input.txt') as f:
    while True:
        line = f.readline()

        if not line:
            break
        word_list.append(line.strip())
    
# print(word_list)

for word in word_list:
    temp_read = ""
    for char in word:
        if char.isdigit():
            temp_read += char
        else:
            continue
    firstDigit = temp_read[0]
    lastDigit = temp_read[len(temp_read)- 1]
    combinedigit = firstDigit + lastDigit
    # print(combinedigit)
    sum += int(combinedigit)

print(sum)

f.close()