#Script para transferência de arquivos entre as coletoras
#Autor: Alberto Dias
#Data: 04/10/2023

import subprocess

DIRETORIO = "/usr/opt/"
file = input("Digite o nome do arquivo a ser transferido: ")

print("Iniciando transferência dos arquivos...")

HOSTS = [
   "IP",
   "IP",
   "IP"
]

for HOST in HOSTS:
   try:
       subprocess.run(
           f'scp "{file}" "user@{HOST}:{DIRETORIO}"',
           shell=True,
           check=True,
       )
       print(f"Transferência de arquivo {file} para {HOST} concluída")
   except subprocess.CalledProcessError as e:
       print(f"Falha na transferência para {HOST}: {e}")
   except Exception as e:
       print(f"Erro inesperado: {e}")

print("Transferência de arquivos concluída")
