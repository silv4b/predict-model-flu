from scripts import gerar_dados as gd, treinar_modelo as tm, executar_predicao as ep


def sair():
    if int(input('Encerrar aplicação? [1 - sim | 0 - não]')) == 1:
        exit(0)


def exec():
    while True:
        if int(input("Treinar modelo com dados fictício? [1 - sim | 0 - não]: ")) == 1:
            print("Executando treinamento com dados fictícios ...")
            gd.gerar_dados(1000)
            tm.treinar_modelo()
            if int(input("Executar questionário? [1 - sim | 0 - não]: ")) == 1:
                ep.executar_predicao()
                sair()
        else:
            print("Executando aplicação com dados fictícios ...")
            ep.executar_predicao()
            sair()


if __name__ == "__main__":
    exec()
