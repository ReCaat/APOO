from BD import BancoDeDados
from User import Usuario
from random import randint
from Email import emailService
from math import pow

class ControleDeAcessos:
# Construtor ----------------------------------------------------------------------
    def __init__(self):
        # cada interface tem um banco de dados
        self.bd = BancoDeDados()
        # a interface inicializa com uma instância de usuário para 
        # representar o nosso ator; ID dado pelo sistema
        user_id = self.__gerarID()
        self.user = Usuario(user_id)
        #sistema de emails
        self.email = emailService("glauco@usp.br")

# Métodos Públicos ----------------------------------------------------------------
    # Interface com o usuário
    def interfaceInicial(self):
        print("Bem vindo ao Sistema Usuário\n")
        
        while(True):
            print("Escolha uma opção: ")
            print("Digite 1 para Login")
            print("Digite 2 para Cadastro")
            print("Digite 3 para sair do Sistema\n")
            
            try: 
                option = int(input())
            except: 
                print("Digite números!\n")
                continue

            if option not in (1, 2, 3):
                print("Opção inválida! Tente novamente \n")
            
            if(option == 1):
                email: str = str(input("Insira o email: "))
                senha: str = str(input("Insira a senha: "))

                self.user.setEmail(email)
                self.user.atualizaSenha(senha)

                result = self.fazerLogin(email, senha)
                login_error_message:str = "Digite 1 e tente fazer Login novamente\n"
                match result:
                    case -1:
                        print("\nEmail não cadastrado\n")
                        print(login_error_message)
                    case -2:
                        print("\nSua senha está errada\n")
                        print(login_error_message)
                    case 1:
                        print("\nSessão iniciada com sucesso\n")
                        self.email.send_mail("Sessão iniciada com sucesso")
                        self.user.logged = True

            if(option == 2):
                nome:str = str(input("Insira o nome: "))
                mail:str = str(input("Insira o email: "))
                senha:str = str(input("Insira a senha: "))

                self.user.setNome(nome)
                self.user.setEmail(mail)
                self.user.atualizaSenha(senha)

                result:int = self.cadastrarUsuario(nome,mail,senha)
                signing_error_message:str = "Digite 2 e tente se cadastrar novamente\n"
                match result:
                    case -1:
                        print("\nEmail já cadastrado\n")
                        print(signing_error_message)
                    case 1:
                        print("Usuário cadastrado com sucesso! Sessão iniciada\n")
                        self.email.send_mail("Conta cadastrada com sucesso")
                        self.user.logged = True

            if(option == 3):
                return

    def iniciarSessao(self):
        print("\nSessão Iniciada\n")
        return True

    def fazerLogin(self, email: str, senha: str):
        usr = self.bd.buscarPorEmail(email)

        if(usr == None):
            return(-1) #email não correspondeu a nada

        if (self.__encriptarSenha(usr.getSenha()) != senha):
            return(-2) #senha errada
        
        return(self.iniciarSessao())
            
    def cadastrarUsuario(self, nome:str, email:str, senha:str):
        usr = self.bd.buscarPorEmail(email)
        if usr is not None:
            return (-1) #email já cadastrado
        
        password:str = self.__encriptarSenha(senha)

        self.bd.salvarUsuario(nome, email, password)

        return(self.iniciarSessao())

# Métodos Privados -----------------------------------------------------------------
    def __gerarID(self, size:int = 6)->str:
        number:int = randint(0, 10**size - 1)
        for i in range(1,size):
            if((number / pow(10,i)) < 0):
                j = size - i
                number = number * pow(10,j)
                break
        
        return str(number)

    def __encriptarSenha(self, senha:str)->str:
        xorKey = 'J'
        for i in range(len(senha)):
        
            senha = (senha[:i] + 
                chr(ord(senha[i]) ^ ord(xorKey)) +
                        senha[i + 1:])
        
        return senha