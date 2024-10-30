# main.py

from scripts import gerar_dados as gd, treinar_modelo as tm, executar_predicao as ep


def sair() -> int:
    if int(input("\nEncerrar aplicação? [1 - sim | 0 - não]: ")) == 1:
        return 1


def exec():
    while True:
        opcao = int(
            input("\nTreinar modelo com dados fictícios? [1 - sim | 0 - não]: ")
        )
        if opcao == 1:
            print("Executando treinamento com dados fictícios ...")
            exibir_df = int(input("Exibir DataFrame? [1 - sim | 0 - não]: "))

            if exibir_df == 1:
                gd.gerar_dados(exibir_df=True)
            else:
                gd.gerar_dados(1000)

            tm.treinar_modelo()
            if int(input("Executar questionário? [1 - sim | 0 - não]: ")) == 1:
                ep.executar_predicao()
                if sair() == 1:
                    break
            else:
                print("Encerrando ...")
                break
        else:
            print("\nExecutando aplicação com dados fictícios salvos ...")
            ep.executar_predicao()
            if sair() == 1:
                break


if __name__ == "__main__":
    exec()
