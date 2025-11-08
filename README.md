# DGT2823 — Trabalho Prático (Pandas)

> Tecnologias para Desenvolvimento de Soluções de Big Data — Estácio  
> **Aluna:** Fernanda Costa — 2025.2

Este repositório contém **todo o projeto** do trabalho prático, incluindo:
- Dataset original (`data/dados.csv`)
- Script de limpeza (`src/limpeza.py`)
- Notebook opcional (`notebooks/trabalho.ipynb`) com as etapas
- Relatório em PDF (`report/Trabalho_Pratico_DGT2823_FernandaCosta.pdf`)

## ✅ Objetivo
Ler, inspecionar e **tratar** o conjunto de dados, padronizando a coluna `Date` para `datetime`, preenchendo nulos em `Calories` com `0` e removendo registros inválidos.

## 🧱 Estrutura
```
dgt2823-projeto/
├── data/
│   ├── dados.csv
├── notebooks/
│   └── trabalho.ipynb
├── report/
│   └── Trabalho_Pratico_DGT2823_FernandaCosta.pdf
├── src/
│   └── limpeza.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠️ Como executar
1. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Rode o script de limpeza:
   ```bash
   python src/limpeza.py --mostrar
   ```
   Isso vai:
   - ler `data/dados.csv` (separador `;`)
   - exibir info/head/tail
   - limpar os dados (ver detalhes abaixo)
   - salvar em `data/dados_limpos.csv`

4. (Opcional) Abra o notebook:
   ```bash
   jupyter notebook notebooks/trabalho.ipynb
   ```

## 🧼 Regras de limpeza aplicadas
- `Calories`: `NaN` → `0`
- `Date`: `NaN` → `'1900/01/01'`
- Correção do valor inválido `20201226` → `'2020/12/26'`
- Conversão de `Date` para `datetime` via `pd.to_datetime(..., format="%Y/%m/%d", errors="coerce")`
- Remoção de linhas com `Date` inválida (`NaT`)

## 🧪 Microatividades (no código)
- Leitura do CSV (`pandas.read_csv`)
- Criação de **subconjunto** de colunas (`ID`, `Date`, `Calories`)
- Configuração `display.max_rows = 9999` (comentada por padrão)
- Exibição de `head` e `tail`
- Uso de `info()` com `memory_usage="deep"`

---

Qualquer dúvida, abra uma issue ou envie mensagem. Boa correção! 🎓
