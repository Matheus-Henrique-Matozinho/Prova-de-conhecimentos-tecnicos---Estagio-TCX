"""

   Descrição: Questão 2 da Prova de conhecimentos técnicos - Estágio TCX
   Elaborado por: Matheus Henrique Martins Matozinho

"""


import cv2
import numpy as np

def carregar_imagem(caminho):
    """
    Carrega uma imagem do caminho especificado.

    Parâmetros:
    - caminho (str): O caminho para a imagem.

    Retorna:
    - np.ndarray: A imagem carregada.
    """
    imagem = cv2.imread(caminho)
    if imagem is None:
        print(f"Erro ao carregar a imagem em {caminho}.")
    return imagem

def detectar_contornos(imagem):
    """
    Detecta contornos em uma imagem usando Canny Edge Detection.

    Parâmetros:
    - imagem (np.ndarray): A imagem na qual os contornos serão detectados.

    Retorna:
    - list: Lista de contornos encontrados.
    """
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    bordas = cv2.Canny(imagem_cinza, 50, 150)
    contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contornos

def desenhar_retangulos(imagem, contornos):
    """
    Desenha retângulos ao redor dos contornos em uma imagem.

    Parâmetros:
    - imagem (np.ndarray): A imagem na qual os retângulos serão desenhados.
    - contornos (list): Lista de contornos.

    Retorna:
    - np.ndarray: A imagem resultante com os retângulos desenhados.
    """
    imagem_resultante = imagem.copy()
    for contorno in contornos:
        x, y, largura, altura = cv2.boundingRect(contorno)
        cv2.rectangle(imagem_resultante, (x, y), (x + largura, y + altura), (0, 255, 0), 2)
    return imagem_resultante

def exibir_imagem(imagem, titulo="Imagem"):
    """
    Exibe uma imagem em uma janela.

    Parâmetros:
    - imagem (np.ndarray): A imagem a ser exibida.
    - titulo (str): O título da janela (padrão: "Imagem").

    """
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Escolha o caminho da imagem que deseja processar
    caminho_imagem = "C:\\Users\\pedro\\Matheus\\pythonProject1\\OPENCV\\Opencv.jpg"

    # Carregar a imagem
    imagem = carregar_imagem(caminho_imagem)

    # Detectar contornos
    contornos = detectar_contornos(imagem)

    # Desenhar retângulos na imagem original
    imagem_resultante = desenhar_retangulos(imagem, contornos)

    # Exibir a imagem resultante
    exibir_imagem(imagem_resultante, "Detecção de Objetos")

if __name__ == "__main__":
    main()
