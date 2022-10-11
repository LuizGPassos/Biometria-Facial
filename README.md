# aps_processamento

Primeira tentativa para o projeto de reconhecimento facial.
A idéia seria fazer o reconhecimento facial ao criar uma câmera virtual (Utilizando a webcam do computador) e fazer a conferencia de autorização a partir de imagens pré-salvas no programa.
Neste código é presente a criação da camera virtual, reconhecimento de face, processamento de imagem para auxiliar a detecção do rosto e com o reconhecimento feito, é desenhado um retângulo ao redor do rosto e alguns pontos espalhados pelo rosto.
Foi descontinuado devido a um problema um uma biblioteca necessária para o reconhecimento facial chamado dlib, que é necessario a instalação da linguagem C++. Devido a estarmos usando um venv (Ambiente virtual python) ocorreu um erro durante a instalação desta biblioteca. Outro problema que tivemos com esse projeto com a virtualização de ambiente foi que o projeto ficou muito pesado. Então fomos para um projeto sem esta funcionalidade.
