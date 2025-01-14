# Conversor de Imagens JPEG para PDF

Este projeto foi desenvolvido para automatizar a conversão de múltiplos arquivos JPEG para o formato PDF, de forma simples e segura. A principal motivação foi a necessidade de enviar diversos documentos em formato PDF para uma plataforma, evitando o uso de soluções online que poderiam comprometer a segurança e privacidade dos documentos.

## Objetivo

A ideia é criar um script para realizar a conversão de arquivos JPEG em PDFs localmente, sem a necessidade de enviar arquivos para servidores de terceiros. Assim, você pode garantir a segurança dos seus documentos ao realizar o processo localmente.

## Como Funciona

Este script percorre todos os arquivos JPEG na pasta onde está sendo executado e os converte para o formato PDF. Para cada arquivo de imagem encontrado, o script cria um PDF com as mesmas dimensões da imagem e a insere no arquivo PDF gerado.

### Dependências

Este script depende das seguintes bibliotecas:

- **Pillow (PIL)**: Usada para abrir e manipular imagens JPEG.
- **ReportLab**: Utilizada para gerar o arquivo PDF.

Você pode instalar as dependências executando o seguinte comando no terminal:

```bash
pip install pillow reportlab
