def simpleEnumeration(A, B, M, d):
    if d >= len(A):
        return

    for j in range(0, len(M[d - 1])):
        e = M[d - 1][j]
        
        if e != 0:
            #αντιγραφή του πίνακα Μ στον Ν
            for p in range(0, len(M)):
                for q in range(0, len(M[0])):
                    N[p][q] = M[p][q]

            #μηδενισμός όλων των μη μηδενικών στοιχείων της γραμμής e του πίνακα Ν, εκτός από τη στήλη e
            for q in range(0, len(N[e])):
                if q != e and N[e][q] != 0:
                    N[e][q] = 0

            #μηδενισμός όλων των μη μηδενικών στοιχείων της στήλης e του πίνακα Ν, εκτός από τη γραμμή e
            for p in range(0, len(N)):
                if p != e and N[p][e] != 0:
                    N[p][e] = 0

            if d == len(A):
                print(N)
            else:
                SimpleEnumeration(A, B, N, d + 1)
                           
#-------------------------------------------------------------------------------------------------------------       
        
def refine(A, B, M):    
    done = False
    
    while not done:
        done = True

        for i in range(0, len(M)):
            rs = 0

            for j in range(0, len(M[0])):
                if M[i][j] != 0:
                    if A[i] != B[j]:
                        M[i][j] = 0
                        done = False
                    else:
                        rs = rs + 1

            if rs = 0:
                return False
            
    return True

#-------------------------------------------------------------------------------------------------------------

def refinedEnumeration(A, B, M, d):
    if d >= len(A):
        return

    for j in range(0, len(M[d - 1])):
        e = M[d - 1][j]
        
        if e != 0:
            #αντιγραφή του πίνακα Μ στον Ν
            for p in range(0, len(M)):
                for q in range(0, len(M[0])):
                    N[p][q] = M[p][q]

            #μηδενισμός όλων των μη μηδενικών στοιχείων της γραμμής e του πίνακα Ν, εκτός από τη στήλη e
            for q in range(0, len(N[e])):
                if q != e and N[e][q] != 0:
                    N[e][q] = 0

            #μηδενισμός όλων των μη μηδενικών στοιχείων της στήλης e του πίνακα Ν, εκτός από τη γραμμή e
            for p in range(0, len(N)):
                if p != e and N[p][e] != 0:
                    N[p][e] = 0

            proceed = refine(A, B, N)

            if proceed:                
                if d == len(A):
                    print(N)
                else:
                    RefinedEnumeration(A, B, N, d + 1)
                
