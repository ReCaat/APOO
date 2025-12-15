class Usuario:
# construtor ----------------------------------------------------------------------
    def __init__(self, id: int):
        self.__Nome = None
        self.__Email = None
        self.__Senha = None
        self.__Id: int = id
        self.__logged: bool=False
# getters -------------------------------------------------------------------------
    def getNome(self) -> str:
        return self.__Nome

    def getId(self) -> int:
        return self.__Id
    
    def isLogged(self) -> bool:
        return self.__logged

    def getEmail(self) -> str:
        return self.__Email
    
    def getSenha(self) -> str:
        return self.__Senha

# setters -------------------------------------------------------------------------
    def setNome(self, novoNome: str):
        self.__Nome = novoNome

    def setLogged(self, newLog: bool):
        self.__logged = newLog

    def setEmail(self, novoEmail: str):
        self.__Email = novoEmail

    def atualizaSenha(self, novaSenha: str):
        self.__Senha = novaSenha
        
