# C2/reconhecimento_yolo.py
from ultralytics import YOLO
import cv2
import os
import numpy as np
from pathlib import Path
from PIL import Image

class ReconhecedorObjetos:
    """
    Sistema de reconhecimento de objetos usando YOLOv8
    Detecta múltiplos objetos em imagens, incluindo gatos e cachorros
    """
    
    def __init__(self, modelo='yolov8n.pt'):
        """
        Inicializa o modelo YOLO
        
        Args:
            modelo: versão do YOLO (n=nano, s=small, m=medium, l=large, x=extra large)
        """
        print("="*60)
        print("RECONHECEDOR DE OBJETOS - YOLOv8")
        print("="*60)
        print(f"\nCarregando modelo {modelo}...")
        self.modelo = YOLO(modelo)  # Baixa automaticamente na primeira vez
        print("✓ Modelo carregado com sucesso!")
        print("="*60 + "\n")
        
    def reconhecer(self, caminho_imagem, salvar_resultado=True):
        """
        Reconhece objetos em uma imagem
        
        Args:
            caminho_imagem: caminho para a imagem
            salvar_resultado: se True, salva imagem com detecções
            
        Returns:
            Lista de objetos detectados
        """
        print(f"Processando: {os.path.basename(caminho_imagem)}")
        
        # Realiza a detecção (.avif precisa ser convertido via Pillow pois YOLO não suporta nativamente)
        if str(caminho_imagem).lower().endswith('.avif'):
            img_pil = Image.open(caminho_imagem).convert('RGB')
            entrada = np.array(img_pil)
        else:
            entrada = caminho_imagem

        resultados = self.modelo(entrada, verbose=False)
        
        # Processa os resultados
        objetos_detectados = []
        for resultado in resultados:
            for box in resultado.boxes:
                classe_id = int(box.cls[0])
                classe_nome = resultado.names[classe_id]
                confianca = float(box.conf[0])
                
                objetos_detectados.append({
                    'classe': classe_nome,
                    'confianca': confianca,
                    'bbox': box.xyxy[0].tolist()  # coordenadas da caixa
                })
        
        # Salva resultado com visualização
        if salvar_resultado:
            pasta_resultado = 'resultados'
            os.makedirs(pasta_resultado, exist_ok=True)
            
            nome_arquivo = os.path.basename(caminho_imagem)
            # cv2.imwrite não suporta .avif — converte a extensão de saída para .jpg
            if nome_arquivo.lower().endswith('.avif'):
                nome_arquivo = os.path.splitext(nome_arquivo)[0] + '.jpg'
            caminho_saida = os.path.join(pasta_resultado, f'detectado_{nome_arquivo}')
            
            # YOLO desenha as caixas automaticamente
            resultado_img = resultados[0].plot()
            cv2.imwrite(caminho_saida, resultado_img)
            print(f"  → Resultado salvo: {caminho_saida}")
        
        return objetos_detectados
    
    def exibir_resultados(self, objetos):
        """Exibe resumo das detecções"""
        if not objetos:
            print("  ⚠ Nenhum objeto detectado nesta imagem\n")
            return
        
        print(f"  ✓ Total detectado: {len(objetos)} objeto(s)")
        
        # Agrupa por classe
        contagem = {}
        for obj in objetos:
            classe = obj['classe']
            contagem[classe] = contagem.get(classe, 0) + 1
        
        # Exibe resumo
        print("  Detecções:")
        for classe, qtd in contagem.items():
            print(f"    - {classe.capitalize()}: {qtd}")
        
        # Exibe detalhes
        print("  Detalhes:")
        for i, obj in enumerate(objetos, 1):
            print(f"    [{i}] {obj['classe'].upper()} - {obj['confianca']:.1%}")
        print()


def buscar_imagens(pasta='imagens_teste'):
    """
    Busca todas as imagens na pasta especificada
    
    Args:
        pasta: caminho da pasta com imagens
        
    Returns:
        Lista de caminhos das imagens encontradas
    """
    pasta_path = Path(pasta)
    
    if not pasta_path.exists():
        return []
    
    # Extensões suportadas
    extensoes = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.webp', '*.avif']
    
    imagens = []
    for ext in extensoes:
        imagens.extend(pasta_path.glob(ext))
    
    return [str(img) for img in imagens]


# Exemplo de uso
if __name__ == "__main__":
    
    # Inicializa o reconhecedor
    reconhecedor = ReconhecedorObjetos(modelo='yolov8n.pt')
    
    # OPÇÃO 1: Buscar imagens locais
    print("Buscando imagens em 'imagens_teste/'...")
    imagens_locais = buscar_imagens('imagens_teste')
    
    if imagens_locais:
        print(f"✓ Encontradas {len(imagens_locais)} imagem(ns)\n")
        print("-"*60)
        
        for i, img in enumerate(imagens_locais, 1):
            print(f"\n[{i}/{len(imagens_locais)}]", end=" ")
            objetos = reconhecedor.reconhecer(img)
            reconhecedor.exibir_resultados(objetos)
            print("-"*60)
    else:
        print("⚠ Nenhuma imagem encontrada em 'imagens_teste/'\n")
        print("TESTANDO COM IMAGENS DA INTERNET...\n")
        print("-"*60)
        
        # OPÇÃO 2: Usar imagens da internet
        imagens_web = [
            'https://ultralytics.com/images/bus.jpg',
            'https://ultralytics.com/images/zidane.jpg',
        ]
        
        for i, url in enumerate(imagens_web, 1):
            print(f"\n[{i}/{len(imagens_web)}]", end=" ")
            try:
                objetos = reconhecedor.reconhecer(url)
                reconhecedor.exibir_resultados(objetos)
            except Exception as e:
                print(f"  ✗ Erro ao processar: {e}")
            print("-"*60)
    
    print("\n" + "="*60)
    print("PROCESSAMENTO CONCLUÍDO!")
    print("="*60)
    print(f"📁 Resultados salvos em: resultados/")
    print("="*60 + "\n")