def calculaMedia(nota1, nota2, nota3):
    return (nota1+nota2+nota3)/3

def validaAprovacao(media):
    if media <= 4:
        print('Reprovado')
    elif media < 6:
        print('Recuperação')
    else:
        print('Aprovado')

def main():
    import sys
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])
    nota3 = float(sys.argv[3])

    media = calculaMedia(nota1, nota2, nota3)
    validaAprovacao(media)

if __name__ == "__main__":
    main()