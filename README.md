# ComprimiRR  

**ComprimiRR** é uma ferramenta simples e eficiente para compressão de arquivos PDF, criada com Python e Ghostscript. 

---

## **Recursos**  

- Compressão de PDFs com diferentes níveis de qualidade:  
  - `screen`: qualidade baixa, menor tamanho.  
  - `ebook`: qualidade moderada, ideal para leitura digital.  
  - `printer`: boa qualidade, tamanho intermediário.  
  - `prepress`: máxima qualidade, para impressão profissional.  
- Automatiza a geração do nome do arquivo comprimido com o sufixo `_comprimido`.  
- Interface de linha de comando (CLI) simples e direta.  
- Exibe a quantidade de páginas do arquivo, o tempo total de execução e a redução percentual de tamanho após a compressão.

---

## **Requisitos**  

- **Python 3.6 ou superior**  
- **Ghostscript** instalado no sistema  
  - Ubuntu/Debian e Derivados:  
    ```bash
    sudo apt install ghostscript
    ```
  - Arch e Derivados:
    ```bash
    sudo pacman -S ghostscript
    ```
  - No Fedora:
    ```bash
    sudo dnf install ghostscript
    ```
  - No macOS:  
    ```bash
    brew install ghostscript
    ```  
  - No Windows: Baixe e instale a partir do site oficial: [Ghostscript Downloads](https://www.ghostscript.com/).  

---

## **Instalação**  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/comprimirr.git
   ```  

2. Navegue até o diretório do projeto:  
   ```bash
   cd comprimirr
   ```  

3. Instale as dependências necessárias (se houver):  
   ```bash
   pip install -r requirements.txt  # Atualmente vazio, mas adicione no futuro se necessário
   ```  

---

## **Como Usar**  

1. Execute o script:  
   ```bash
   python3 comprimirr.py
   ```  

2. Informe o caminho do arquivo PDF que deseja comprimir.  

3. Escolha o nível de qualidade:  
   - `screen`  
   - `ebook`  
   - `printer`  
   - `prepress`  

4. O arquivo comprimido será gerado no mesmo diretório do original com o sufixo `_comprimido`.  

---

## **Exemplo**  

Entrada: `relatorio.pdf`  
Saída: `relatorio_comprimido.pdf`  

```bash
$ python3 comprimirr.py
Digite o caminho para o arquivo PDF de entrada: relatorio.pdf
Escolha a qualidade (screen, ebook, printer, prepress): ebook
Comprimindo relatorio.pdf com qualidade 'ebook'...
PDF comprimido salvo em: relatorio_comprimido.pdf
Total de páginas: 120
Tempo total de execução: 35.67 segundos
Redução de tamanho: 72.56%
Tamanho original: 10.23 MB
Tamanho comprimido: 2.80 MB
```

---

## **Contribuições**  

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:  

1. Faça um fork do repositório.  
2. Crie uma branch para a sua feature ou correção:  
   ```bash
   git checkout -b minha-feature
   ```  
3. Commit suas alterações:  
   ```bash
   git commit -m "Adicionei minha feature"
   ```  
4. Faça o push para a branch:  
   ```bash
   git push origin minha-feature
   ```  
5. Abra um Pull Request.  

---
