import os
from openai import OpenAI

# 🔑 COLOQUE SUA CHAVE AQUI
API_KEY = "CHAVE_API_AQUI"

client = OpenAI(api_key=API_KEY) if API_KEY != "SUA_CHAVE_AQUI" else None

# 🎨 CORES
class C:
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    CYAN    = '\033[96m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    WHITE   = '\033[97m'
    BOLD    = '\033[1m'
    RESET   = '\033[0m'

# 🤖 IA
def ia_resposta(prompt):
    if client is None:
        return "⚠️ IA desativada (adicione sua API_KEY para ativar)"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um professor de Python direto, didático e objetivo."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na IA: {e}"

# 🧠 MODO EXPLICAÇÃO
def modo_explicacao(contexto):
    print(C.YELLOW + C.BOLD + "\n" + "━" * 50 + C.RESET)
    print(C.YELLOW + C.BOLD + "  🧠  MODO EXPLICAÇÃO COM IA" + C.RESET)
    print(C.YELLOW + "  📚 Tema: " + C.WHITE + contexto + C.RESET)
    print(C.YELLOW + C.BOLD + "━" * 50 + C.RESET)

    while True:
        print(C.MAGENTA + "  📤 /sair → voltar ao quiz" + C.RESET)
        print(C.BLUE + "  " + "─" * 46 + C.RESET)
        user = input(C.YELLOW + "  💬 Sua dúvida: " + C.RESET).strip()

        if user.lower() == "/sair":
            print(C.CYAN + "\n  ↩️  Voltando ao quiz...\n" + C.RESET)
            break

        print(C.YELLOW + "\n  🤖 IA respondendo...\n" + C.RESET)
        resposta = ia_resposta(f"Contexto: {contexto}\nPergunta do aluno: {user}")
        print(C.YELLOW + "  " + "─" * 46 + C.RESET)
        print(C.WHITE + resposta + C.RESET)
        print(C.YELLOW + "  " + "─" * 46 + C.RESET)

# ❓ PERGUNTA
def ask_question(pergunta, alternativas, resposta, contexto):
    while True:
        print(C.BLUE + "\n  " + "━" * 46 + C.RESET)
        print(C.CYAN + C.BOLD + "  ❓ " + pergunta + C.RESET)
        print(C.BLUE + "  " + "━" * 46 + C.RESET)
        for alt in alternativas:
            print(C.WHITE + "     " + alt + C.RESET)
        print(C.BLUE + "  " + "─" * 46 + C.RESET)
        print(C.MAGENTA + "  💡 /explique → pedir ajuda à IA" + C.RESET)
        print(C.BLUE + "  " + "─" * 46 + C.RESET)
        user = input(C.YELLOW + "  👉 Sua resposta (a/b/c/d): " + C.RESET).strip()

        if user == "/explique":
            modo_explicacao(contexto)
            continue

        if user.lower() == resposta.lower():
            print(C.GREEN + C.BOLD + "\n  ✅  CORRETO! Muito bem! 🎉\n" + C.RESET)
            break
        else:
            print(C.RED + C.BOLD + "\n  ❌  Errado! A resposta correta era: " + C.YELLOW + C.BOLD + resposta.upper() + C.RESET)
            print(C.RED + "  🔄  A IA vai criar uma nova pergunta sobre este tema...\n" + C.RESET)

            nova = ia_resposta(f"""
Crie uma nova pergunta de múltipla escolha sobre: {contexto}

Formato EXATO:
Pergunta: [texto]
a) [opção A]
b) [opção B]
c) [opção C]
d) [opção D]
Resposta: [letra]
💡 Dica: [explicação didática curta]

Seja objetivo, claro e educativo.
""")

            print(C.YELLOW + "\n" + nova + C.RESET)

# 🧩 DESAFIO
ICONES = {1:"📥",2:"🖨️ ",3:"🔄",4:"➕",5:"📐",6:"🔢",7:"🎨",8:"📏",9:"🔁",10:"🔗",11:"🏆"}

def desafio(numero, perguntas, contexto):
    icone = ICONES.get(numero, "🎯")
    print(C.YELLOW + C.BOLD + "\n" + "═" * 50 + C.RESET)
    print(C.YELLOW + C.BOLD + f"  {icone}  DESAFIO {numero}: {contexto.upper()}" + C.RESET)
    print(C.YELLOW + C.BOLD + "═" * 50 + C.RESET)
    for p in perguntas:
        ask_question(p["pergunta"], p["alternativas"], p["resposta"], contexto)
    print(C.GREEN + C.BOLD + f"\n  ✅  Desafio {numero} concluído!\n" + C.RESET)

# � TUTORIAL
def tutorial():
    print(C.GREEN + C.BOLD + "\n" + "═" * 50 + C.RESET)
    print(C.GREEN + C.BOLD + "    🔥  QUIZ PYTHON COM IA  🔥" + C.RESET)
    print(C.GREEN + C.BOLD + "═" * 50 + C.RESET)
    print(C.CYAN + """
  Bem-vindo! Este quiz te ensina tudo que precisa
  para completar o DESAFIO FINAL. 🎯

  📋 COMO FUNCIONA:
  ┌─────────────────────────────────────────────┐
  │  • Leia a pergunta e as 4 alternativas      │
  │  • Digite a letra (a, b, c ou d) + Enter    │
  │  • Acertou → próxima pergunta     ✅        │
  │  • Errou  → IA cria nova pergunta ❌        │
  └─────────────────────────────────────────────┘

  💡 COMANDOS (sempre visíveis durante o quiz):
  ┌─────────────────────────────────────────────┐
  │  /explique → abre chat com a IA             │
  │  /sair     → volta ao quiz (do /explique)   │
  └─────────────────────────────────────────────┘

  🏁 SEU OBJETIVO FINAL:
  ┌─────────────────────────────────────────────┐
  │  Criar programa que:                        │
  │  1. Peça nome do usuário                    │
  │  2. Calcule área (largura × comprimento)    │
  │  3. Calcule litros de tinta (área ÷ 2)      │
  │  4. Mostre tabuada da área (for + range)    │
  │  5. Converta metros → cm e mm              │
  └─────────────────────────────────────────────┘""" + C.RESET)
    input(C.YELLOW + C.BOLD + "\n  ▶  Pressione Enter para começar..." + C.RESET)
    print()

# 🚀 MAIN
def main():
    tutorial()

    desafios = [
    (1, [
        {"pergunta": "O que faz a função input() em Python?",
         "alternativas": ["a) Exibe texto na tela",
                          "b) Lê o que o usuário digita e retorna como texto",
                          "c) Realiza cálculos matemáticos",
                          "d) Cria variáveis automaticamente"],
         "resposta": "b"},

        {"pergunta": "Como guardar o NOME do usuário em uma variável?",
         "alternativas": ["a) nome = print('Qual seu nome? ')",
                          "b) nome = int('Qual seu nome? ')",
                          "c) nome = input('Qual seu nome? ')",
                          "d) nome = 'nome'"],
         "resposta": "c"},

        {"pergunta": "input() SEMPRE retorna qual tipo de dado?",
         "alternativas": ["a) int  (número inteiro)",
                          "b) float  (número decimal)",
                          "c) bool  (verdadeiro/falso)",
                          "d) str  (texto/string)"],
         "resposta": "d"},
    ], "entrada de dados com input()"),

    (2, [
        {"pergunta": "Qual função exibe informações na tela?",
         "alternativas": ["a) input()",
                          "b) show()",
                          "c) print()",
                          "d) display()"],
         "resposta": "c"},

        {"pergunta": "Com nome='Ana', qual mostra 'Olá, Ana!' corretamente?",
         "alternativas": ["a) print('Olá, nome!')",
                          "b) print(f'Olá, {nome}!')",
                          "c) print('Olá, ' + nome + '!')",
                          "d) Tanto b) quanto c) funcionam"],
         "resposta": "d"},

        {"pergunta": "f-strings são iniciadas com qual letra antes das aspas?",
         "alternativas": ["a) s  →  s'texto'",
                          "b) r  →  r'texto'",
                          "c) f  →  f'texto'",
                          "d) b  →  b'texto'"],
         "resposta": "c"},
    ], "exibindo dados com print() e f-strings"),

    (3, [
        {"pergunta": "input() retorna str. Para usar em cálculo, convertemos com:",
         "alternativas": ["a) str()  — mantém como texto",
                          "b) int() ou float()  — converte para número",
                          "c) bool()  — converte para verdadeiro/falso",
                          "d) Não precisa converter, Python faz sozinho"],
         "resposta": "b"},

        {"pergunta": "O que resulta int('10') + 5 ?",
         "alternativas": ["a) '105'  (concatenação de texto)",
                          "b) Erro de execução",
                          "c) 10.5",
                          "d) 15  (soma numérica)"],
         "resposta": "d"},

        {"pergunta": "Para receber a LARGURA de uma sala (pode ter decimais):",
         "alternativas": ["a) largura = input('Largura: ')",
                          "b) largura = int(input('Largura: '))",
                          "c) largura = float(input('Largura: '))",
                          "d) largura = str(input('Largura: '))"],
         "resposta": "c"},
    ], "conversão de tipos: int() e float()"),

    (4, [
        {"pergunta": "Qual símbolo representa MULTIPLICAÇÃO em Python?",
         "alternativas": ["a) x  (letra x)",
                          "b) ×  (símbolo matemático)",
                          "c) *  (asterisco)",
                          "d) .  (ponto)"],
         "resposta": "c"},

        {"pergunta": "Para calcular área = largura VEZES comprimento:",
         "alternativas": ["a) area = largura + comprimento",
                          "b) area = largura - comprimento",
                          "c) area = largura * comprimento",
                          "d) area = largura / comprimento"],
         "resposta": "c"},

        {"pergunta": "10 / 4 em Python retorna qual valor?",
         "alternativas": ["a) 2  (arredonda para baixo)",
                          "b) 3  (arredonda para cima)",
                          "c) 2.5  (divisão com decimal)",
                          "d) Erro de tipo"],
         "resposta": "c"},
    ], "operadores: *, /, +, -"),

    (5, [
        {"pergunta": "Área mede qual grandeza de uma superfície plana?",
         "alternativas": ["a) O comprimento de uma borda (1 dimensão)",
                          "b) O espaço bidimensional ocupado (superfície)",
                          "c) O volume de espaço ocupado (3 dimensões)",
                          "d) O peso do material da superfície"],
         "resposta": "b"},

        {"pergunta": "Para calcular área de uma sala RETANGULAR, precisamos:",
         "alternativas": ["a) Apenas o comprimento",
                          "b) Apenas a largura",
                          "c) Largura E comprimento (duas medidas)",
                          "d) Largura, comprimento E altura (três medidas)"],
         "resposta": "c"},

        {"pergunta": "A unidade correta para área de cômodos é:",
         "alternativas": ["a) metros (m)  — comprimento linear",
                          "b) metros quadrados (m²)  — área de superfície",
                          "c) centímetros (cm)  — comprimento pequeno",
                          "d) litros (L)  — volume de líquidos"],
         "resposta": "b"},
    ], "conceito de área"),

    (6, [
        {"pergunta": "Sala de 4m de largura e 5m de comprimento. Qual a área?",
         "alternativas": ["a) 9 m²   (4 + 5  →  soma)",
                          "b) 1 m²   (5 - 4  →  subtração)",
                          "c) 0.8 m²  (4 / 5  →  divisão)",
                          "d) 20 m²  (4 × 5  →  multiplicação)"],
         "resposta": "d"},

        {"pergunta": "Em Python, como calcular a área da sala com variáveis?",
         "alternativas": ["a) area = largura + comprimento",
                          "b) area = largura * comprimento",
                          "c) area = largura / comprimento",
                          "d) area = largura ** comprimento"],
         "resposta": "b"},

        {"pergunta": "Se largura = 3.5 e comprimento = 6.0, então area = ?",
         "alternativas": ["a) 9.5   (3.5 + 6.0)",
                          "b) 18.0  (3.0 × 6.0)",
                          "c) 21.0  (3.5 × 6.0)",
                          "d) 2.5   (6.0 - 3.5)"],
         "resposta": "c"},
    ], "calculando área na prática"),

    (7, [
        {"pergunta": "1 litro de tinta cobre 2m². Para pintar 10m², precisamos:",
         "alternativas": ["a) 2 litros   (10 - 2×4 — errado)",
                          "b) 20 litros  (10 × 2  — quantidade total)",
                          "c) 5 litros   (10 ÷ 2  — correto!)",
                          "d) 8 litros"],
         "resposta": "c"},

        {"pergunta": "A fórmula correta para calcular litros de tinta é:",
         "alternativas": ["a) tinta = area + rendimento_por_litro",
                          "b) tinta = area * rendimento_por_litro",
                          "c) tinta = rendimento_por_litro / area",
                          "d) tinta = area / rendimento_por_litro"],
         "resposta": "d"},

        {"pergunta": "Se area = 24m² e 1 litro cobre 3m², quantos litros?",
         "alternativas": ["a) 72 litros  (24 × 3  — errado)",
                          "b) 27 litros  (24 + 3  — errado)",
                          "c) 8 litros   (24 ÷ 3  — correto!)",
                          "d) 21 litros  (24 - 3  — errado)"],
         "resposta": "c"},
    ], "calculando litros de tinta"),

    (8, [
        {"pergunta": "1 metro equivale a quantos centímetros?",
         "alternativas": ["a) 10 cm   (× 10)",
                          "b) 100 cm  (× 100)",
                          "c) 1000 cm (× 1000)",
                          "d) 0.1 cm  (÷ 10)"],
         "resposta": "b"},

        {"pergunta": "Para converter metros em centímetros em Python:",
         "alternativas": ["a) cm = metros - 100",
                          "b) cm = metros / 100",
                          "c) cm = metros + 100",
                          "d) cm = metros * 100"],
         "resposta": "d"},

        {"pergunta": "2.5 metros = quantos milímetros? (1m = 1000mm)",
         "alternativas": ["a) 250 mm   (2.5 × 100)",
                          "b) 25 mm    (2.5 × 10)",
                          "c) 2500 mm  (2.5 × 1000)",
                          "d) 0.25 mm  (2.5 ÷ 10)"],
         "resposta": "c"},
    ], "conversão de unidades: m, cm, mm"),

    (9, [
        {"pergunta": "Qual estrutura repete código um número definido de vezes?",
         "alternativas": ["a) if / else  — executa se condição for verdadeira",
                          "b) def        — define uma função",
                          "c) for        — laço de repetição",
                          "d) return     — retorna valor de função"],
         "resposta": "c"},

        {"pergunta": "range(1, 11) gera quais números?",
         "alternativas": ["a) De 0 até 11 (total: 12 números)",
                          "b) De 1 até 11 (total: 11 números)",
                          "c) De 1 até 10 (total: 10 números)",
                          "d) De 0 até 10 (total: 11 números)"],
         "resposta": "c"},

        {"pergunta": "Para mostrar a TABUADA de 4 (4×1 até 4×10):",
         "alternativas": ["a) for i in range(11): print(4 * i)",
                          "b) for i in range(1, 11): print(f'4 x {i} = {4*i}')",
                          "c) for i in range(1, 10): print(4 * i)",
                          "d) for i in (1, 11): print(4 * i)"],
         "resposta": "b"},
    ], "loops com for e range()"),

    (10, [
        {"pergunta": "No programa final, qual deve ser a PRIMEIRA ação?",
         "alternativas": ["a) Calcular a área da sala",
                          "b) Mostrar a tabuada da área",
                          "c) Converter metros em cm",
                          "d) Pedir nome e medidas com input()"],
         "resposta": "d"},

        {"pergunta": "Com area=20.0, como mostrar a tabuada da área?",
         "alternativas": ["a) print(area * 10)",
                          "b) for i in range(area): print(i)",
                          "c) for i in range(1, 11): print(f'{area} x {i} = {area*i}')",
                          "d) while area > 0: print(area)"],
         "resposta": "c"},

        {"pergunta": "Qual é a ordem CORRETA das etapas do programa final?",
         "alternativas": ["a) Calcular → Pedir dados → Mostrar → Converter",
                          "b) Tabuada → Calcular → Pedir dados → Converter",
                          "c) Converter → Calcular → Pedir dados → Mostrar",
                          "d) Pedir dados → Calcular → Mostrar → Tabuada → Converter"],
         "resposta": "d"},
    ], "estrutura do programa final"),

    (11, [
        {"pergunta": "largura=5, comprimento=4, 1L cobre 2m². Litros de tinta?",
         "alternativas": ["a) 5 litros   (calculou só largura)",
                          "b) 10 litros  (area=20, tinta=20÷2=10  ✓)",
                          "c) 20 litros  (esqueceu de dividir)",
                          "d) 40 litros  (multiplicou tudo)"],
         "resposta": "b"},

        {"pergunta": "Com area=15.0, como exibir 'Área: 15.0 m²' com f-string?",
         "alternativas": ["a) print('Área: ' + area + ' m²')  — erro de tipo",
                          "b) print('Área: {area} m²')  — falta o f",
                          "c) print(f'Área: {area} m²')  — correto!",
                          "d) print('Área: area m²')  — imprime a palavra"],
         "resposta": "c"},

        {"pergunta": "Qual linha lê a LARGURA da sala como número decimal?",
         "alternativas": ["a) largura = input('Largura: ')  — retorna str",
                          "b) largura = int(input('Largura: '))  — sem decimal",
                          "c) float largura = input('Largura: ')  — sintaxe errada",
                          "d) largura = float(input('Largura: '))  — correto!"],
         "resposta": "d"},
    ], "revisão geral — pronto para o desafio!"),
    ]

    for d in desafios:
        desafio(*d)

    print(C.GREEN + C.BOLD + "\n" + "═" * 50 + C.RESET)
    print(C.GREEN + C.BOLD + "  🏁  DESAFIO FINAL  🏁" + C.RESET)
    print(C.GREEN + C.BOLD + "═" * 50 + C.RESET)
    print(C.CYAN + """
  Você passou pelos 11 desafios! Hora de juntar
  tudo e criar seu programa completo. 💪

  📝 CRIE UM PROGRAMA QUE:

  1️⃣   nome = input('Seu nome: ')
  2️⃣   largura = float(input('Largura da sala (m): '))
        comprimento = float(input('Comprimento (m): '))
  3️⃣   area = largura * comprimento
  4️⃣   tinta = area / 2   (1 litro cobre 2m²)
  5️⃣   for i in range(1, 11):
            print(f'{area} x {i} = {area * i}')
  6️⃣   cm = area * 10000   (m² → cm²)
        mm = area * 1000000  (m² → mm²)

  💡 Use f-strings para exibir todos os resultados!
  🔥 Use TUDO que você aprendeu nos 11 desafios!
""" + C.RESET)
    print(C.GREEN + C.BOLD + "═" * 50 + C.RESET)

if __name__ == "__main__":
    main()