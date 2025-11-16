# 🎯 Jogo da Adivinhação (CLI)

[![PyPI version](https://badge.fury.io/py/jogo-da-adivinhacao-renan-martins.svg)](https://pypi.org/project/jogo-da-adivinhacao-renan-martins/)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Jogo direto no terminal: você pensa em um número entre **1 e 63** e o programa descobre qual é só fazendo algumas perguntas.  

---

## Instalação

### Linux/Mac (bash)

```bash
pip install jogo-da-adivinhacao-renan-martins
```

### Windows (PowerShell)

```powershell
pip install jogo-da-adivinhacao-renan-martins
```

---

## Como executar

Depois de instalar, é só rodar:

```bash
jogo-adivinha
```

---

## Como jogar

1. **Pense** em um número entre 1 e 63 
2. **Responda** `s` ou `n` para cada cartela que aparecer
3. **Veja** o programa adivinhar seu número em 6 perguntas!

##Atualização

Para atualizar para a versão mais recente:

```bash
pip install --upgrade jogo-da-adivinhacao-renan-martins
```

---

## Como funciona?

O jogo usa **representação binária** dos números:
- Cada cartela representa um bit específico
- Suas respostas "montam" o número em binário

**Exemplo:** Se você pensou em **13**:
- Binário: `1101`
- Temos 3 bits ligados (1) e 1 bit desligado (0)
- Olhando da direita para esquerda:
    - Cartela 1 (1): Sim 
    - Cartela 2 (2): Não
    - Cartela 3 (4): Sim
    - Cartela 4 (8): Sim
- Somando os primeiros valores das cartelas respondidas com "Sim": 1 + 4 + 8 = **13** ✓

---

## Links úteis

- **PyPI:** https://pypi.org/project/jogo-da-adivinhacao-renan-martins/
- **Repositório:** https://github.com/renanrodm/jogo-da-adivinhacao
- **Issues:** https://github.com/renanrodm/jogo-da-adivinhacao/issues

---

## Autor

**Renan Martins**  
- renanrodm@gmail.com  
- [@renanrodm](https://github.com/renanrodm)
- Desenvolvido como projeto educacional