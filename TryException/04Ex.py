# Crie uma função divisao_segura(a, b) que retorne o resultado da divisão a / b.
# Se b for zero, a função deve retornar "Erro: Divisão por zero não permitida!".

n = input('Indique um número para o numerador:')
d = input('Indique um número para o denominado: ')


def divisao_segura(n, d):
    try:
        # Convertendo para número
        n = float(n)
        d = float(d)

        # Verifica se o denominador é zero
        if d == 0:
            return "Erro: Divisão por zero não permitida!"

        return n / d  # Retorna o resultado da divisão

    except ValueError:  # Captura erro de conversão caso entrada seja inválida
        return "Erro: Entrada inválida! Insira apenas números."


# Chamando a função e verificando o resultado
resultado = divisao_segura(n, d)

# Se o resultado for um número, formata com duas casas decimais
if isinstance(resultado, float):
    print(f'Resultado: {resultado:.2f}')
else:
    print(resultado)  # Exibe a mensagem de erro sem tentar formatar


