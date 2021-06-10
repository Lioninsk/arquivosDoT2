import memory_profiler


@memory_profiler.profile
def checa_primo(n):
    if n == 1:
        return False    
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False     
    return True

def n_primo(n):
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

print(f"Resposta:{n_primo(10)}\n")
