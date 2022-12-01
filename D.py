res = []
for _ in range(int(input())) :
    n = int(input())
    A = list(map(int, input().split()))

    Ld = [a%10 for a in A]

    if (5 in Ld or 0 in Ld) :
        for i in range(n) :
            if Ld[i] == 5 :
                A[i] += 5
        if len(set(A)) == 1 :
            res.append("YES")
        else :
            res.append("NO")
        continue

    for i in range(n) :
        if Ld[i] == 1 :
            A[i] += 7
        elif Ld[i] == 2 :
            A[i] += 6
        elif Ld[i] == 3 :
            A[i] += 15
        elif Ld[i] == 4 :
            A[i] += 4
        elif Ld[i] == 6 :
            A[i] += 12
        elif Ld[i] == 7 :
            A[i] += 11
        elif Ld[i] == 9 :
            A[i] += 9
    
    for i in range(n-1) :
        if (A[i]-A[i+1])%20 != 0 :
            res.append("NO")
            break
    else :
        res.append("YES")

print(*res, sep='\n')