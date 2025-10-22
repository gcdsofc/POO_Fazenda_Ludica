# Classe base - Animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som."

    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."


# Subclasse 1 - Cachorro
class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"


# Subclasse 2 - Gato
class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"


# Subclasse 3 - Vaca (com encapsulamento)
class Vaca(Animal):
    def __init__(self, nome, idade, producao_leite_litros):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros  # atributo privado

    def emitir_som(self):
        return "Muuu!"

    # Getter (obter_producao_leite)
    def obter_producao_leite(self):
        return self.__producao_leite_litros

    # Setter (registrar_ordenha)
    def registrar_ordenha(self, litros):
        if litros >= 0:
            self.__producao_leite_litros = litros
        else:
            print("Quantidade inválida de leite!")


# ============================
# TESTE E DEMONSTRAÇÃO
# ============================

if __name__ == "__main__":
    # Criando os objetos
    cachorro = Cachorro("Rex", 3, "Labrador")
    gato = Gato("Mimi", 5, "Branco")
    vaca = Vaca("Mimosa", 7, 25.5)

    # Apresentação
    print(cachorro.apresentar())
    print(gato.apresentar())
    print(vaca.apresentar())

    print()  # Linha em branco para separar a saída

    # Sons
    print(f"{cachorro.nome} diz: {cachorro.emitir_som()}")
    print(f"{gato.nome} diz: {gato.emitir_som()}")
    print(f"{vaca.nome} diz: {vaca.emitir_som()}")

    print()  # Linha em branco

    # Teste de encapsulamento
    print(f"Produção atual de leite da {vaca.nome}: {vaca.obter_producao_leite()} litros")

    vaca.registrar_ordenha(28.0)
    print(f"Nova produção de leite da {vaca.nome}: {vaca.obter_producao_leite()} litros")
