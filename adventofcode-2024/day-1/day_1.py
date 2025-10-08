left_list = []
right_list = []
list = []
distance_list = []
total_distance = 0


def main():
    if len(left_list) == len(right_list):
        # print(f"Length of the list is {len(left_list)} ids")
        readfile('locations_list.txt')
    else:
        print("List has uneven pair of location ids")

    split_list()
    sort_list()
    
    # print(list)
    # print(left_list)
    # print(right_list)

    calculate_distance()
    similarity_score = calculate_similarity_score()

    print(f"The Total Distance is {total_distance}")
    print(f"The Similarity Score is {similarity_score}")

def readfile(filename):
    # Read the file and split into two lists
    with open (filename) as f:
        while True:
            line = f.readline()

            if not line:
                break

            list.append(line.strip())

def sort_list():
    left_list.sort()
    right_list.sort()


def split_list():
    for item in list:
        # print(item)
        l,r = item.split()

        left_list.append(int(l))
        right_list.append(int(r))

def calculate_distance():
    global total_distance

    for i in range(len(left_list)):
        dist = abs(left_list[i] - right_list[i])
        distance_list.append(dist)
    
    # print(distance_list)

    for dis in distance_list:
         total_distance += dis

def calculate_similarity_score():
    sim_score = 0
    for i in left_list:
        for j in right_list:
            if i == j:
                sim_score += j
            else:
                continue

    return sim_score
if __name__ == "__main__":
    main()