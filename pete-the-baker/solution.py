#UTF-8
#Code from the repository "https://github.com/mignoe/coding-challenges"
#Author: Miguel de Oliveira Rodrigues (username: mignoe)
#email: miguel.rodrigues@ccc.ufcg.edu.br

def cakes(recipe, available):
    num = []
    for i in recipe:
        if i in available:
            num.append(available[i] // recipe[i]) 
        else:
            return 0
    num.sort()
    return num[0]

