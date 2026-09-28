import os
import google.generativeai as genai

# 1. Configuração da API
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("ERRO: Configure a variável de ambiente GEMINI_API_KEY antes de rodar.")
    exit()

genai.configure(api_key=api_key)

# 2. Carregando a Base de Conhecimento
def carregar_conhecimento():
    caminho_arquivo = os.path.join(os.path.dirname(__file__), '../data/base_conhecimento.txt')
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Erro: Base de conhecimento não encontrada."

base_conhecimento = carregar_conhecimento()

# 3. Configurando o Prompt de Sistema e o Modelo
instrucoes_sistema = f"""
Você é a Bia Resgate, especialista em ajudar brasileiros a saírem das dívidas.
Regra 1: Baseie suas respostas ESTRITAMENTE no texto delimitado por ### abaixo.
Regra 2: Nunca invente informações financeiras, taxas ou regras que não estejam no texto.
Regra 3: Se o usuário fizer uma pergunta que não pode ser respondida pelo texto base, diga: "Desculpe, minha especialidade foca estritamente nas regras da minha base de conhecimento para não colocar as suas finanças em risco. Como posso ajudar com a priorização das suas dívidas?"
Regra 4: Seja empática e prática.

### BASE DE CONHECIMENTO ###
{base_conhecimento}
### FIM DA BASE DE CONHECIMENTO ###
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    system_instruction=instrucoes_sistema
)

chat = model.start_chat(history=[])

# 4. Interface de Conversa no Terminal
print("=====================================================")
print("BIA RESGATE: INICIANDO ATENDIMENTO")
print("=====================================================\n")
print("Bia: Olá! Eu sou a Bia. Estou aqui para te ajudar a organizar as suas dívidas e limpar seu nome. Qual é o seu maior problema hoje?")

while True:
    usuario = input("\nVocê: ")
    if usuario.lower() in ['sair', 'quit', 'tchau']:
        print("Bia: Lembre-se: um passo de cada vez. Vou estar aqui quando precisar. Até logo!")
        break
    
    resposta = chat.send_message(usuario)
    print(f"\nBia: {resposta.text}")
