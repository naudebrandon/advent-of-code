levels_list = []
safe = 0

def main():
    global safe
    # load_file("Day 2 Test.txt")
    load_file("Day 2.txt")

    for line in levels_list:
        inc_dec = check_increase_decrease(line)
        diff = check_level_difference(line)

        if inc_dec and diff:
            safe += 1
    
    print(f"Safe {safe}")



def check_increase_decrease(line):
    valid = False
    num_list = line.split()

    if int(num_list[0]) > int(num_list[1]):
        # All must be smaller
        for j in range(len(num_list)-1):
            if int(num_list[j]) > int(num_list[j + 1]):
                valid = True
            else:
                valid = False
                break

    if int(num_list[0]) < int(num_list[1]):
        # All must be larger
        for k in range(len(num_list)-1):
            if int(num_list[k]) < int(num_list[k + 1]):
                valid = True
            else:
                valid = False
                break

    return valid
            


def check_level_difference(line):
    valid = False
    num_list = line.split()

    for j in range(len(num_list)-1):
            difference = int(num_list[j]) - int(num_list[j + 1])
            if abs(difference) < 4:
                valid = True
            else:
                valid = False
                break

    return valid

def load_file(filename):
     # Read the file into memory --> levels_list
    with open (filename) as f:
        while True:
            line = f.readline()

            if not line:
                break

            levels_list.append(line.strip())

if __name__ == "__main__":
    main()