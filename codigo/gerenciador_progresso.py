import json
import os
from vidas import Vidas

class GerenciadorProgresso:
    def __init__(self):
        self.__pontuacao = 0
        self.__vidas = 0
        self.__caminho_arquivo = os.path.join(os.path.dirname(__file__), "progresso.json")
        self.__dados = None  

    #region Setters e Getters
    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, valor):
        self.__pontuacao = valor

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, valor):
        self.__vidas = valor

    @property
    def caminho_arquivo(self):
        return self.__caminho_arquivo

    @caminho_arquivo.setter
    def caminho_arquivo(self, valor):
        self.__caminho_arquivo = valor

    #endregion

    def salvar_progresso(self, pontuacao, vidas):
        try:
            dados = {
                "pontuacao": pontuacao,
                "vidas": vidas
            }
            with open(self.caminho_arquivo, "w") as f:
                json.dump(dados, f, indent=4)
            print("💾 Progresso salvo com sucesso.")
        except Exception as erro:
            print(f"⚠️ [PROGRESSO] Erro ao salvar progresso: {erro}")

    def carregar_progresso(self):
        try:
            if not os.path.exists(self.caminho_arquivo):
                print("⚠️ [PROGRESSO] Nenhum arquivo de progresso encontrado.")
                self.dados = None
                return None

            with open(self.caminho_arquivo, "r") as f:
                dados = json.load(f)
                self.pontuacao = dados.get("pontuacao", 0)
                self.vidas = dados.get("vidas", 3)
                self.__dados = dados
                print("📂 Progresso carregado com sucesso.")
                return dados

        except Exception as erro:
            print(f"⚠️ [PROGRESSO] Erro ao carregar progresso: {erro}")
            self.__dados = None
            return None

    def deletar_progresso(self):
        try:
            if os.path.exists(self.caminho_arquivo):
                os.remove(self.caminho_arquivo)
                self.dados = None
                print("🗑️ Progresso deletado.")
        except Exception as erro:
            print(f"⚠️ [PROGRESSO] Erro ao deletar progresso: {erro}")

    def aplicar_progresso(self, jogo):
        if not self.dados:
            print("⚠️ [PROGRESSO] Nenhum dado carregado para aplicar.")
            return False
        
        jogo.pontuacao = self.dados.get('pontuacao', 0)
        vidas_salvas = self.dados.get('vidas', 3)

        jogo.lista_vidas.clear()
        jogo.grupo_vidas.empty()

        for i in range(vidas_salvas):
            x = jogo.tela.largura - (i * (40 + 5))
            vida = Vidas(jogo.grupo_vidas, x)
            jogo.lista_vidas.append(vida)

        print("✅ Progresso aplicado ao jogo.")
        return True
