import subprocess
import os
import PyPDF2
import time
import sys

# Função para contar o número de páginas do PDF
def contar_paginas_pdf(input_pdf):
    try:
        with open(input_pdf, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            return len(reader.pages)
    except Exception as e:
        print(f"Erro ao contar páginas do PDF: {e}")
        return None

# Função para calcular a redução percentual de tamanho
def calcular_reducao_tamanho(input_pdf, output_pdf):
    try:
        # Obter os tamanhos dos arquivos
        tamanho_antes = os.path.getsize(input_pdf)
        tamanho_depois = os.path.getsize(output_pdf)

        # Calcular a redução percentual
        if tamanho_antes > 0:
            percentual_reducao = ((tamanho_antes - tamanho_depois) / tamanho_antes) * 100
            return percentual_reducao, tamanho_antes, tamanho_depois
        else:
            return 0, tamanho_antes, tamanho_depois
    except Exception as e:
        print(f"Erro ao calcular a redução de tamanho: {e}")
        return 0, 0, 0

# Função para comprimir o PDF
def comprimir_pdf(input_pdf, qualidade="screen"):
    base_nome = os.path.splitext(os.path.basename(input_pdf))[0]
    output_pdf = f"{base_nome}_comprimido.pdf"

    comando = [
        "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/" + qualidade,
        "-dNOPAUSE", "-dBATCH",
        "-sOutputFile=" + output_pdf, input_pdf
    ]

    # Contar páginas no PDF
    total_paginas = contar_paginas_pdf(input_pdf)
    if total_paginas is None:
        print("Não foi possível contar as páginas do PDF.")
        return None

    try:
        print(f"Comprimindo {input_pdf} com qualidade '{qualidade}'...")
        start_time = time.time()  # Inicia o cronômetro

        # Executar o comando de compressão real
        processo = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        tempo_decorrido = time.time() - start_time  # Tempo total de execução
        if processo.returncode == 0:
            print(f"\nPDF comprimido salvo em: {output_pdf}")
            print(f"Total de páginas: {total_paginas}")
            print(f"Tempo total de execução: {tempo_decorrido:.2f} segundos")
            
            # Calcular a redução de tamanho
            percentual_reducao, tamanho_antes, tamanho_depois = calcular_reducao_tamanho(input_pdf, output_pdf)
            print(f"Redução de tamanho: {percentual_reducao:.2f}%")
            print(f"Tamanho original: {tamanho_antes / (1024 * 1024):.2f} MB")
            print(f"Tamanho comprimido: {tamanho_depois / (1024 * 1024):.2f} MB")
            
            return output_pdf
        else:
            print(f"Erro ao comprimir o PDF. Código de retorno: {processo.returncode}")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Erro ao comprimir o PDF: {e}")
        return None
    except FileNotFoundError:
        print("Ghostscript não encontrado. Certifique-se de que está instalado e acessível no PATH.")
        return None

if __name__ == "__main__":
    input_pdf = input("Digite o caminho para o arquivo PDF de entrada: ").strip()
    qualidade = input("Escolha a qualidade (screen, ebook, printer, prepress): ").strip()

    if not os.path.exists(input_pdf):
        print("Arquivo PDF de entrada não encontrado.")
    else:
        comprimido = comprimir_pdf(input_pdf, qualidade)
        if comprimido:
            print(f"\nArquivo comprimido gerado: {comprimido}")
