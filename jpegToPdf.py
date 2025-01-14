from PIL import Image
from reportlab.pdfgen import canvas
import os

# Função para converter JPEG para PDF
def converter_jpeg_para_pdf(imagem, pdf_file):
    # Abrir o arquivo JPEG
    image = Image.open(imagem)

    # Criar um PDF com as dimensões da imagem
    c = canvas.Canvas(pdf_file, pagesize=(image.width, image.height))

    # Adicionar a imagem ao PDF
    c.drawImage(imagem, 0, 0, width=image.width, height=image.height)

    # Salvar o PDF
    c.save()
    print(f"PDF {pdf_file} criado com sucesso!")

# Verificar se a pasta 'PDF' existe, se não, criá-la
if not os.path.exists("PDF"):
    os.makedirs("PDF")

# Loop para converter todos os arquivos JPEG em PDF na pasta atual
for file in os.listdir():
    if file.endswith(".jpeg"):
        # Caminho do PDF a ser salvo dentro da pasta PDF
        caminho_pdf = os.path.join("PDF", file.replace(".jpeg", ".pdf"))
        converter_jpeg_para_pdf(file, caminho_pdf)
