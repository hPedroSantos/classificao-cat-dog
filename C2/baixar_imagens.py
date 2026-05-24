# C2/baixar_imagens.py

import urllib.request
import os
from pathlib import Path

def baixar_imagens_teste():
    """
    Baixa automaticamente um conjunto de imagens para testar o YOLO
    Imagens gratuitas do Unsplash (sem direitos autorais)
    """
    
    print("="*60)
    print("DOWNLOAD DE IMAGENS DE TESTE")
    print("="*60)
    
    # Cria pasta se não existir
    pasta_destino = Path('C2/imagens_teste')
    pasta_destino.mkdir(parents=True, exist_ok=True)
    
    # Lista de imagens para baixar (URLs do Unsplash - gratuitas)
    imagens = {
        'gato_cachorro_01.jpg': 'https://images.unsplash.com/photo-1450778869180-41d0601e046e?w=1200&q=80',
        'gato_cachorro_02.jpg': 'https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=1200&q=80',
        'cachorro_parque_01.jpg': 'https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=1200&q=80',
        'cachorro_parque_02.jpg': 'https://images.unsplash.com/photo-1477884213360-7e9d7dcc1e48?w=1200&q=80',
        'gato_casa_01.jpg': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=1200&q=80',
        'gato_casa_02.jpg': 'https://images.unsplash.com/photo-1574158622682-e40e69881006?w=1200&q=80',
        'pets_multiplos_01.jpg': 'https://images.unsplash.com/photo-1415369629372-26f2fe60c467?w=1200&q=80',
        'pets_multiplos_02.jpg': 'https://images.unsplash.com/photo-1444212477490-ca407925329e?w=1200&q=80',
    }
    
    print(f"\n📥 Iniciando download de {len(imagens)} imagens...\n")
    
    sucesso = 0
    falhas = 0
    
    for nome_arquivo, url in imagens.items():
        caminho_destino = pasta_destino / nome_arquivo
        
        # Pula se já existe
        if caminho_destino.exists():
            print(f"⏭  {nome_arquivo} - já existe, pulando...")
            sucesso += 1
            continue
        
        try:
            print(f"⬇  Baixando: {nome_arquivo}...", end=' ')
            
            # Baixa a imagem
            urllib.request.urlretrieve(url, caminho_destino)
            
            # Verifica tamanho
            tamanho = caminho_destino.stat().st_size / 1024  # KB
            print(f"✓ ({tamanho:.0f} KB)")
            
            sucesso += 1
            
        except Exception as e:
            print(f"✗ ERRO: {e}")
            falhas += 1
    
    # Resumo
    print("\n" + "="*60)
    print("RESUMO DO DOWNLOAD")
    print("="*60)
    print(f"✓ Sucesso: {sucesso}/{len(imagens)}")
    print(f"✗ Falhas: {falhas}/{len(imagens)}")
    print(f"📁 Pasta: {pasta_destino.absolute()}")
    print("="*60 + "\n")
    
    if sucesso > 0:
        print("✅ Imagens prontas para usar!")
        print(f"   Execute agora: python C2/reconhecimento_yolo.py\n")
    else:
        print("⚠ Nenhuma imagem foi baixada. Verifique sua conexão.\n")

if __name__ == "__main__":
    baixar_imagens_teste()