if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #print(arr)
    res = [*set(arr)]
    #print(res)
    res.sort()
    print(res[-2])
