import random

LENGTH = 50
impactDiameter = LENGTH / 10
impacts = [0]
time = 0
impact = 0.0
BLANKS = ' '
CENTER = '+'
IMPACT = 'x'
RING = '#'
assumption = 0.15

grid = [[BLANKS for x in range(LENGTH)] for x in range(LENGTH)]

def makeCrater(grid):
    a = random.randrange(0, LENGTH-1)
    b = random.randrange(0, LENGTH-1)
    for i in range(int((impactDiameter/2))+2):
        for j in range(int(((impactDiameter//2)+2)-i/2)):
            if(a+i >= LENGTH):
                if(b+j >= LENGTH):
                    grid[a][b-j] = RING
                    grid[a-i][b-j] = RING
                    grid[a-i][b] = RING
                if(b-j <= 0):
                    grid[a][b+j] = RING
                    grid[a-i][b] = RING
                    grid[a-i][b+j] = RING
                if(b+j < LENGTH and b-j > 0):
                    grid[a][b-j] = RING
                    grid[a][b+j] = RING
                    grid[a-i][b-j] = RING
                    grid[a-i][b+j] = RING
            if(a - i < 0):
                if(b+j >= LENGTH):
                    grid[a][b-j] = RING
                    grid[a+i][b-j] = RING
                    grid[a+i][b] = RING
                if(b-j < 0):
                    grid[a][b+j] = RING
                    grid[a+i][b] = RING
                    grid[a+i][b+j] = RING
                if(b+j < LENGTH and b-j > 0):
                    grid[a][b-j] = RING
                    grid[a][b+j] = RING
                    grid[a+i][b-j] = RING
                    grid[a+i][b+j] = RING
            if(b+j >= LENGTH):
                if(a+i >= LENGTH):
                    grid[a-i][b] = RING
                    grid[a-i][b-j] = RING
                    grid[a][b-j] = RING
                if(a-i <= 0):
                    grid[a-i][b] = RING
                    grid[a-i][b-j] = RING
                    grid[a][b-j] = RING
                if((a+i < LENGTH) and a-i > 0):
                    grid[a-i][b] = RING
                    grid[a+i][b] = RING
                    grid[a-i][b-j] = RING
                    grid[a+i][b-j] = RING
            if(b-j <= 0):
                if(a+i >= LENGTH):
                    grid[a-i][b] = RING
                    grid[a-i][b+j] = RING
                    grid[a][b+j] = RING
                if(a-i <= 0):
                    grid[a-i][b] = RING
                    grid[a-i][b+j] = RING
                    grid[a][b+j] = RING
                if(a+i < LENGTH and a-i > 0):
                    grid[a-i][b] = RING
                    grid[a+i][b] = RING
                    grid[a-i][b+j] = RING
                    grid[a+i][b+j] = RING
            if(b+j < LENGTH and b-j >= 0 and a+i < LENGTH and a-i >= 0):
                grid[a-i][b-j] = RING
                grid[a+i][b-j] = RING
                grid[a-i][b+j] = RING
                grid[a+i][b+j] = RING
    for i in range(int((impactDiameter/2)+1)):
        for j in range(int(((impactDiameter/2)+1)-i/2)):
            if(a+i >= LENGTH):
                if(b+j >= LENGTH):
                    grid[a][b-j] = IMPACT
                    grid[a-i][b-j] = IMPACT
                    grid[a-i][b] = IMPACT
                if(b-j <= 0):
                    grid[a][b+j] = IMPACT
                    grid[a-i][b] = IMPACT
                    grid[a-i][b+j] = IMPACT
                if(b+j < LENGTH and b-j > 0):
                    grid[a][b-j] = IMPACT
                    grid[a][b+j] = IMPACT
                    grid[a-i][b-j] = IMPACT
                    grid[a-i][b+j] = IMPACT
            if(a - i < 0):
                if(b+j >= LENGTH):
                    grid[a][b-j] = IMPACT
                    grid[a+i][b-j] = IMPACT
                    grid[a+i][b] = IMPACT
                if(b-j < 0):
                    grid[a][b+j] = IMPACT
                    grid[a+i][b] = IMPACT
                    grid[a+i][b+j] = IMPACT
                if(b+j < LENGTH and b-j > 0):
                    grid[a][b-j] = IMPACT
                    grid[a][b+j] = IMPACT
                    grid[a+i][b-j] = IMPACT
                    grid[a+i][b+j] = IMPACT
            if(b+j >= LENGTH):
                if(a+i >= LENGTH):
                    grid[a-i][b] = IMPACT
                    grid[a-i][b-j] = IMPACT
                    grid[a][b-j] = IMPACT
                if(a-i <= LENGTH):
                    grid[a-i][b] = IMPACT
                    grid[a-i][b-j] = IMPACT
                    grid[a][b-j] = IMPACT
                if((a+i < LENGTH) and a-i > 0):
                    grid[a-i][b] = IMPACT
                    grid[a+i][b] = IMPACT
                    grid[a-i][b-j] = IMPACT
                    grid[a+i][b-j] = IMPACT
            if(b-j <= 0):
                if(a+i >= LENGTH):
                    grid[a-i][b] = IMPACT
                    grid[a-i][b+j] = IMPACT
                    grid[a][b+j] = IMPACT
                if(a-i <= 0):
                    grid[a-i][b] = IMPACT
                    grid[a-i][b+j] = IMPACT
                    grid[a][b+j] = IMPACT
                if(a+i < LENGTH and a-i > 0):
                    grid[a-i][b] = IMPACT
                    grid[a+i][b] = IMPACT
                    grid[a-i][b+j] = IMPACT
                    grid[a+i][b+j] = IMPACT
            if(b+j < LENGTH and b-j >= 0 and a+i < LENGTH and a-i >= 0):
                grid[a-i][b-j] = IMPACT
                grid[a+i][b-j] = IMPACT
                grid[a-i][b+j] = IMPACT
                grid[a+i][b+j] = IMPACT
        grid[a][b] = CENTER
    return grid

def numImpacts(grid):
    impact = 0
    for i in range(LENGTH-1):
        for j in range(LENGTH-1):
            if(grid[i][j] == CENTER):
                impact += 1.0
    return impact

def determineIfSaturated(impacts, time):
    if time == 0:
        curAvg = 0.0
        oldAvg = 0.0
    else:
        if (time // 2) == 0:
            curAvg = impacts[time] / time if time != 0 else 0
            oldAvg = 0.0
        else:
            curAvg = impacts[time] / time if time != 0 else 0
            oldAvg = impacts[time // 2] / (time // 2)
    if time // 2 == 0:
        return False
    if abs(impacts[time] - impacts[time // 2]) < impacts[time // 2] * assumption:
        if impacts[time] < 5:
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    while not determineIfSaturated(impacts, time):
        crater = random.randrange(1, 1000)
        if crater == 666:
            grid = makeCrater(grid)
        impacts.append(numImpacts(grid))
        if time % 30000 == 0:
            print("\nTime =", time, "Impacts= ", impacts[time])
            for x in grid:
                print(' '.join(x))
        time += 1

    print("\nTime vs Impacts")
    for x in grid:
        print(' '.join(x))
    print("# of impacts: ", numImpacts(grid))
    print("Yrs to Saturation: ", time)
    print("Time | # of Impacts")
    for i in range(len(impacts)):
        if i % 10000 == 0:
            print(i, "|", impacts[i])