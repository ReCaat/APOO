class Usuario:
# construtor ----------------------------------------------------------------------
    def __init__(self, id: int):
        self.__Id: int = id
        self.logged: bool = False

# getters -------------------------------------------------------------------------
    def getNome(self) -> str:
        return self.__Nome

    def getEmail(self) -> str:
        return self.__Email
    
    def getSenha(self) -> str:
        return self.__Senha

# setters -------------------------------------------------------------------------
    def setNome(self, novoNome: str):
        self.__Nome = novoNome

    def setEmail(self, novoEmail: str):
        self.__Email = novoEmail

    def atualizaSenha(self, novaSenha: str):
        self.__Senha = novaSenha
        
