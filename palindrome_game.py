import collections

string = input().upper()

box = collections.Counter()

winner = False

for i in range(len(string)):
    #print(string)
    if (i % 2) == 0:
        # alice's turn
        # string[0] or string[-1]
        
        box[string[0]] += 1
        for item in box:
            if box[item] == 2:
                string = string[1:]
                winner = True
                print("Alice")
                break
        
        if not winner:
            box[string[0]] -= 1
            box[string[-1]] += 1
            string = string[:-1]
            for item in box:
                if box[item] == 2:
                    winner = True
                    print("Alice")
                    break

    elif (i % 2) != 0:
        # bob's turn
        
        box[string[0]] += 1
        for item in box:
            if box[item] == 2:
                string = string[1:]
                winner = True
                print("Bob")
                break
        
        if not winner:
            box[string[0]] -= 1
            box[string[-1]] += 1
            string = string[:-1]
            for item in box:
                if box[item] == 2:
                    winner = True
                    print("Bob")
                    break

    if winner:
        break

if not winner:
    print("Tie")
