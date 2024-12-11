

filename = "input-04.txt"

with open(filename, "r") as in_file:
    data = in_file.read().split("\n")
data = data[:-1]
dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def check(x, y, grid):
    num = 0
    oldx = x
    oldy = y
    for tup in dirs:
        x = oldx
        y = oldy
        
        xmod = tup[0]
        ymod = tup[1]

        vals = ['M', 'A', 'S']
        found = True
        for val in vals:
            x += xmod
            y += ymod

            
            if x < 0 or x >= len(grid):
                found = False
                break

            if y < 0 or y >= len(grid[x]):
                found = False
                break

            if grid[x][y] != val:
                found = False
                break
        if found:
            num += 1

    return num

corners = [set([0,2,5,7])]
def checkmas(x,y,grid):

    ans = 0
    oldx = x
    oldy = y
    found = set()
    for i,tup in enumerate(dirs):
        try:
            x = oldx
            y = oldy
            
            xmod = tup[0]
            ymod = tup[1]

            minx = x - xmod
            maxx = x + xmod
            miny = y - ymod
            maxy = y + ymod

            #print((minx,miny), (maxx,maxy))
            if minx < 0 or minx >= len(grid):
                continue

            if maxx < 0 or maxx >= len(grid):
                continue
            
            if miny < 0 or miny >= len(grid[0]):
                continue

            if maxy < 0 or maxy >= len(grid[0]):
                continue

            if grid[minx][miny] == 'M' and grid[maxx][maxy] == 'S':
                found.add(i)
                
        except:
            print(oldx, oldy)
    for corner in corners:
        if len(corner.intersection(found)) == 2:
            ans += 1
    return ans

total = 0
totalmas = 0

for (i, line) in enumerate(data):
    tmp = False
    for(j, cell) in enumerate(line):
        if cell == 'X':
            total += check(i,j, data)
        if cell == 'A':
            totalmas += checkmas(i,j,data)
            
print(total)
print(totalmas)
