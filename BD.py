import pandas as pd
from User import Usuario
from pathlib import Path

class BancoDeDados:
    def __init__(self, caminho_csv="usuarios.csv"):
        self.caminho = Path(caminho_csv)

        # abrindo o CSV caso exista ou criando do contrário
        if self.caminho.exists():
            self.df = pd.read_csv(self.caminho)
        else:
            self.df = pd.DataFrame(
                columns=["id", "nome", "email", "senha"]
            )

        self._write_csv()

# Métodos Públicos do BD -----------------------------------------------------------
    def buscarPorEmail(self, email: str):
        resultado = self.df[self.df["email"] == email]

        if resultado.empty:
            return None

        # retornando o usúario
        linha = resultado.iloc[0]
        user = Usuario(int(linha["id"]))
        user.setEmail(linha["email"])
        user.setNome(linha["nome"])
        user.atualizaSenha(linha["senha"])

        return user

    def salvarUsuario(self, nome: str, email: str, senha: str)->Usuario:
        if self.buscarPorEmail(email):
            raise ValueError("Usuário com esse email já existe")

        novo_id = self._next_id()

        novo_registro = {
            "id": novo_id,
            "nome": nome,
            "email": email,
            "senha": senha
        }

        self.df = pd.concat(
            [self.df, pd.DataFrame([novo_registro])],
            ignore_index=True
        )

        self._write_csv()

        user = Usuario(novo_id)
        user.atualizaSenha(senha)
        user.setEmail(email)
        user.setNome(nome)
        return user
    
# Métodos Privados -----------------------------------------------------------------
    def _write_csv(self):
        self.df.to_csv(self.caminho, index=False)

    def _next_id(self):
        if self.df.empty:
            return 1
        return int(self.df["id"].max()) + 1

