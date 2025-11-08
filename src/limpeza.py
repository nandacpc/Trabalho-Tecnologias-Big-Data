# -*- coding: utf-8 -*-

"""
Trabalho Prático — DGT2823
Tecnologias para Desenvolvimento de Soluções de Big Data

Script de limpeza e preparação de dados conforme roteiro do trabalho.
Autor(a): Fernanda Costa
"""

import argparse
import pandas as pd
from pathlib import Path

def carregar_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, sep=';', engine='python')
    return df

def microatividade_config_visualizacao(df: pd.DataFrame):
    # Configura exibição
    pd.set_option("display.max_rows", 9999)
    print("\n[Microatividade 3] DataFrame completo (to_string):")
    print(df.to_string())

def microatividade_subconjunto(df: pd.DataFrame) -> pd.DataFrame:
    subset_cols = ["ID", "Date", "Calories"]
    sub = df[subset_cols].copy()
    print("\n[Microatividade 2] Subconjunto de colunas:", subset_cols)
    print(sub.head())
    return sub

def exibir_primeiras_ultimas(df: pd.DataFrame, n: int = 10):
    print(f"\n[Microatividade 4] Primeiras {n} linhas:")
    print(df.head(n))
    print(f"\n[Microatividade 4] Últimas {n} linhas:")
    print(df.tail(n))

def info_geral(df: pd.DataFrame):
    print("\n[Microatividade 5] Informações gerais:")
    print(df.info(memory_usage="deep"))

def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df_limpo = df.copy()

    # 7a) Substitui NaN em Calories por 0
    df_limpo["Calories"] = df_limpo["Calories"].fillna(0)

    # 8a) Substitui NaN em Date por '1900/01/01'
    df_limpo["Date"] = df_limpo["Date"].fillna("1900/01/01")

    # 10) Corrige valor '20201226' -> '2020/12/26'
    df_limpo["Date"] = df_limpo["Date"].replace("20201226", "2020/12/26")

    # 8c/9b) Converte Date para datetime, marcando inválidos como NaT
    df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d", errors="coerce")

    # 12) Remove registros com Date nulo (NaT)
    df_limpo = df_limpo.dropna(subset=["Date"]).reset_index(drop=True)

    return df_limpo

def main():
    parser = argparse.ArgumentParser(description="Limpeza do dataset do Trabalho Prático DGT2823.")
    parser.add_argument("--input", default="data/dados.csv", help="Caminho do CSV de entrada.")
    parser.add_argument("--output", default="data/dados_limpos.csv", help="Caminho do CSV de saída.")
    parser.add_argument("--mostrar", action="store_true", help="Mostra info/heads/tails durante a execução.")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    print("[1] Lendo CSV:", in_path)
    df = carregar_csv(in_path)

    if args.mostrar:
        print("\n[2] Visualização inicial")
        info_geral(df)
        exibir_primeiras_ultimas(df, 10)

        print("\n[3] Subconjunto (3 colunas)")
        _ = microatividade_subconjunto(df)

        print("\n[4] Alterando configuração de exibição (max_rows=9999)")
        # Atenção: imprimir tudo pode ser verboso; manter comentado por padrão.
        # microatividade_config_visualizacao(df)

    print("\n[5] Iniciando limpeza...")
    df_limpo = limpar_dados(df)

    if args.mostrar:
        print("\n[6] Resultado após limpeza:")
        info_geral(df_limpo)
        exibir_primeiras_ultimas(df_limpo, 10)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df_limpo.to_csv(out_path, sep=';', index=False)
    print(f"\n[7] Arquivo salvo em: {out_path.resolve()}")

if __name__ == "__main__":
    main()
