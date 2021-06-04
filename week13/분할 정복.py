import sys
def searching(r,c,d):
    global counter
    if r+d > rs and c+d > cs:
        if d > 1:
            searching(r,c,d/2)
            searching(r,c+d/2, d / 2)
            searching(r+d/2, c, d / 2)
            searching(r+d/2, c+d/2, d / 2)
        else:
            if r == rs and c == cs:
                print(int(counter))
                sys.exit(0)
            elif r == rs and c+d == cs:
                counter+=1
                print(int(counter))
                sys.exit(0)
            elif r+d == rs and c == cs:
                counter+=2
                print(int(counter))
                sys.exit(0)
            elif r+d == rs and c+d == cs:
                counter+=3
                print(int(counter))
                sys.exit(0)
            else:
                counter += 4
                return 0
    else:
        counter += d*d
        return
    return
if __name__ == '__main__':
    n,rs,cs = map(int,input().split(" "));
    counter = 0
    searching(0,0,pow(2,n))