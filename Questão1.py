"""

   Descrição: Prova de conhecimentos técnicos - Estágio TCX
   Elaborado por: Matheus Henrique Martins Matozinho

"""
import cv2
import numpy as np

def aplicar_filtros(imagem_path, limiar=127):
    """
        Aplica uma série de filtros a uma imagem e exibe as imagens resultantes.

        Parâmetros:
        - imagem_path (str): Caminho para a imagem a ser processada.
        - limiar (int): Valor de limiar para a limiarização (padrão: 127).
    """

    # Carregar a imagem
    imagem = cv2.imread(imagem_path)

    # Verificar se a imagem foi carregada corretamente
    if imagem is None:
        print(f"Erro ao carregar a imagem em {imagem_path}.")
        return

    # a) Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # b) Aplicar um filtro de média com um kernel 3x3
    kernel = np.ones((3, 3), np.float32) / 9
    imagem_filtrada = cv2.filter2D(imagem_cinza, -1, kernel)

    # c) Aplicar limiarização adaptativa
    imagem_limiarizada = cv2.adaptiveThreshold(imagem_filtrada, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Salvar a imagem resultante
    cv2.imwrite("imagem_resultante.png", imagem_limiarizada)

    # Exibir as imagens original, em escala de cinza, filtrada e limiarizada
    exibir_imagens({
        "Imagem Original": imagem,
        "Imagem em Escala de Cinza": imagem_cinza,
        "Imagem Filtrada": imagem_filtrada,
        "Imagem Limiarizada": imagem_limiarizada
    })

def exibir_imagens(imagens):
    """
       Exibe imagens em janelas separadas com seus respectivos nomes.

       Parâmetro:
       - imagens (dict): Dicionário contendo pares de nome e imagem.
    """

    for nome, img in imagens.items():
        cv2.imshow(nome, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    """
        Função principal para carregar uma imagem, chamar a função aplicar_filtros e salvar a imagem resultante.
    """
    # Chamar a função com o caminho da imagem desejada e um limiar de sua escolha
    imagem_path = "C:\\Users\\pedro\\Matheus\\pythonProject1\\OPENCV\\Opencv.jpg"
    aplicar_filtros(imagem_path)

if __name__ == "__main__":
    main()

