score_dict = {}
try:
    read_scores = open("highest scores/scores.txt", "r")
    for line in read_scores.readlines():
        line = line.strip().split(":")
        if line[0] in score_dict:
            if int(score_dict[line[0]]) < int(line[1]):
                score_dict[line[0]] = line[1]
        else:
            score_dict[line[0]] = line[1]
    read_scores.close()
except:
    print("no scores to read")


quit = False
while not quit:mike
    name = input("enter name: " ).lower()
    if name in score_dict.keys():
        print(score_dict[name])
    elif name == "quit":
        quit = True
    else:
        print("name not in dictonary")