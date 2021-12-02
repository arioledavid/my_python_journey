def countingValleys(steps, path):

    level = 0
    valleys = 0

    for i in range(steps):
        print(path[i])
        if path[i] == 'D':
            print("down takes 1")
            level -= 1
            if path[i] == 'D' and level == -1:
                valleys += 1
        elif path[i] == 'U':
            print("up adds 1")
            level += 1
        print(f"level = {level} from sea level")
    print(f"{valleys} valeys encountered")


path = 'UDDDUUDUUDUUDD'
steps = 14
countingValleys(steps, path)

