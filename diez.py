def Calculate(c, d):
    return (112*c) + (75*d)


clowns = int(input("Enter number of clowns: "))
dolls = int(input("Enter number of dolls: "))
weight = Calculate(clowns, dolls)
print(f"Total Weight: {weight}")
