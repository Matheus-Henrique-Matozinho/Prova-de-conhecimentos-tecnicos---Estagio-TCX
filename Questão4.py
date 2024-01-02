"""
Descrição: Questão 4 da Prova de conhecimentos técnicos - Estágio TCX
   Elaborado por: Matheus Henrique Martins Matozinho

Resposta:   
QUESTÃO 4)
O OpenCV oferece diversas transformações geométricas para manipulação de imagens, permitindo ajustes como translação, rotação, redimensionamento e perspectiva. Cada uma dessas transformações é crucial em diferentes contextos de visão computacional.

Translação: A translação desloca a posição da imagem em relação a um eixo. É útil para ajustar a posição de objetos na cena. Por exemplo, ao rastrear um objeto em movimento, a translação pode ser usada para compensar sua mudança de posição.

Rotação: A rotação gira a imagem em torno de um ponto específico. É aplicada em cenários como orientação de objetos ou correção de inclinações. Por exemplo, ao alinhar um objeto em uma imagem, a rotação pode ser usada para endireitá-lo.

Redimensionamento: O redimensionamento ajusta o tamanho da imagem. Isso é útil para padronizar tamanhos de entrada em modelos de visão computacional ou para reduzir a complexidade computacional. Por exemplo, ao treinar um modelo de reconhecimento de objetos, redimensionar as imagens para um tamanho específico pode ser necessário.

Perspectiva: A transformação de perspectiva corrige distorções causadas por ângulos de visão. Pode ser empregada em aplicações como correção de distorções em imagens capturadas por câmeras. Por exemplo, ao mapear uma imagem em um plano tridimensional, a transformação de perspectiva é crucial para preservar a forma correta dos objetos.

As transformações geométricas são representadas por matrizes de transformação. Cada operação tem sua matriz específica, e as operações podem ser combinadas multiplicando as matrizes. No OpenCV, a função cv::warpAffine é frequentemente utilizada para aplicar transformações lineares, enquanto a função cv::warpPerspective é usada para transformações de perspectiva. Essas funções levam como parâmetro a matriz de transformação desejada, permitindo uma aplicação eficiente e flexível dessas operações em imagens.
"""
