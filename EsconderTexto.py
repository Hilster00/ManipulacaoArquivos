def esconder_texto(pdf_original, novo_pdf, texto):
    with open(pdf_original, "rb") as arquivo_lido:
        bytes_arquivo = arquivo_lido.read()
        
        # Defina as marcas para identificar o início e o fim do texto oculto
        inicio = b"\x00BEGIN_TEXT"
        fim = b"\x01END_TEXT"
        
        # Adicione o marcador de início e o texto oculto ao PDF
        bytes_arquivo += inicio + texto.encode("utf-8") + fim
        
        with open(novo_pdf, "wb") as novo_pdf:
            novo_pdf.write(bytes_arquivo)

if __name__ == "__main__":
    pdf_original = f"{input('Nome do arquivo:')}.pdf"
    pdf_texto_escondido = f"{input('Nome do novo arquivo:')}.pdf"
    texto_esconder = input("Digite o texto que deseja ocultar:")
    
    esconder_texto(pdf_original, pdf_texto_escondido, texto_esconder)
    print("Texto oculto adicionado ao PDF com sucesso!")
