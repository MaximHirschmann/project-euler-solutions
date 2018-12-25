with open("storage//13.txt","r") as f:
    print(str(sum(map(int,f.read().split("\n"))))[:10])
