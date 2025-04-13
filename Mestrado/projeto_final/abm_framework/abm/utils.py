import time

def medir_tempo_execucao(func: callable) -> callable:
    def wrapper(*args: tuple, **kwargs: dict) -> any:
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"[⏱️] Tempo de execução de {func.__name__}: {fim - inicio:.2f}s")
        return resultado
    return wrapper
