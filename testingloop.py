a=input("What operation do you want to use?: ")
    
for red in a:
    if a=="combinations":
        from itertools import combinations

        x=input("Enter the minimum number: ")
        if x == "return":
            continue
        else:
            y=input("Enter the maximum number: ")
            if y == "return":
                continue
            else:
                z=input(f'Enter x as in {y}Cx: ')
                if z == "return":
                    continue
                else:
                    x=int(x)
                    y=int(y)
                    z=int(z)

                    rng= range(x,y)

                    counting=0

                    for i in combinations(rng,z):
                        print(i)
                        counting+=1

                    print(f' In total {counting} {a}. Jeez!')


    elif a=="permutations":
        from itertools import permutations

        x=input("Enter the minimum number: ")
        if x == "return":
            continue
        else:
            y=input("Enter the maximum number: ")
            if y == "return":
                continue
            else:
                z=input(f'Enter x as in {y}Px: ')
                if z == "return":
                    continue
                else:
                    k=int(x)
                    l=int(y)
                    m=int(z)

                    rng= range(k,l)

                    counting=0

                    for i in permutations(range(k,l),m):
                        print(i)
                        counting+=1

                    print(f' In total {counting} {a}. Jeez!')
    break
