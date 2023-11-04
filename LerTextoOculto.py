def ler_texto_oculto(pdf_ler):
    with open(pdf_ler, "rb") as pdf_ler:
        bytes_pdf = pdf_ler.read()
        
        # Defina as marcas para identificar o início e o fim do texto oculto
        inicio = b"\x00BEGIN_TEXT"
        fim = b"\x01END_TEXT"
        
        inicio_posicao = bytes_pdf.find(inicio)
        fim_posicao = bytes_pdf.find(fim)
        
        if inicio_posicao != -1 and fim_posicao != -1:
            texto_oculto = bytes_pdf[inicio_posicao + len(inicio):fim_posicao].decode("utf-8")
            return texto_oculto
        else:
            return "Texto oculto não encontrado no PDF."

if __name__ == "__main__":
    pdf = f"{input('Digite o nome do arquivo:')}.pdf"  #
    texto = ler_texto_oculto(pdf)
    
    print("Texto oculto no PDF:", texto)
