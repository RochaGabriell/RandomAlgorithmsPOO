def um(n):
    return "1"

def dois(n):
    return "2"

def tres(n):
    return "3"

def outros(n):
    return "..."

n = 3

acao = {1: um, 2: dois, 3: tres} # Informar as confições com a opcão(chava), depois os modulos de cada uma

acao = acao.get(n, outros) # Informa o chave ecistente, se n tiver entra na default

print(acao(n))