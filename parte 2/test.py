import cProfile


def checa_primo(n):
    """
    n: numero natural.
    Retorna True se um numero e primo
    e False caso o contrario.
    """
    if n == 1:
        return False    
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False     
    return True


def n_primo(n):
    """
    n: numero natural.
    Encontra o enesimo primo.
    """
    if n == 1:
        return 2
    else:
        counter = 1
        candidate = 1
        
        while counter < n:
            if candidate//10 == 3:
                candidate += 4
            else:
                candidate += 2
            if checa_primo(candidate):
                counter += 1   
    return candidate

    
pr = cProfile.Profile()
pr.enable()
print(f"Resposta:{n_primo(1000)}\n")
pr.disable()
pr.print_stats()