
---

## 📋 Índice
- [C1 - Classificação de Imagens](#c1---classificação-de-imagens-gato-vs-cachorro)
- [C2 - Reconhecimento de Objetos](#c2---reconhecimento-de-objetos-com-yolov8)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)

---

## C1 - Classificação de Imagens (Gato vs Cachorro)

### 📝 Descrição
Modelo de classificação binária que identifica se uma imagem contém **gato** ou **cachorro**.

### 🛠️ Tecnologias Utilizadas
- Python 3.x
- TensorFlow / Keras
- CNN (Convolutional Neural Network)

### 📁 Arquivos
- Código disponível na pasta `C1/`

---

## C2 - Reconhecimento de Objetos com YOLOv8

### 📝 Descrição
Sistema de **detecção e reconhecimento** de múltiplos objetos em imagens usando **YOLOv8 (You Only Look Once)**.

Diferente da C1 que apenas classifica uma imagem, este sistema:
- ✅ Detecta **múltiplos objetos** na mesma imagem
- ✅ Localiza objetos com **caixas delimitadoras** (bounding boxes)
- ✅ Reconhece **80 classes** diferentes (COCO dataset)
- ✅ Funciona em **tempo real**

### 🎯 Algoritmo Escolhido: YOLOv8 (Nano)

#### Por que YOLOv8?

1. **Velocidade e Eficiência**
   - Detecção em tempo real mesmo em CPU
   - Versão "nano" otimizada para rapidez

2. **Precisão**
   - Modelo pré-treinado no dataset COCO
   - 80 classes reconhecidas com alta acurácia

3. **Facilidade de Uso**
   - Biblioteca Ultralytics moderna e bem documentada
   - Instalação simples com pip
   - API intuitiva

4. **Visualização Automática**
   - Desenha caixas e labels automaticamente
   - Facilita demonstração e análise

5. **Versatilidade**
   - Funciona com imagens estáticas, vídeos e streams
   - Não requer GPU (embora seja mais rápido com GPU)

### 📊 Classes Reconhecidas

O modelo YOLOv8 reconhece **80 classes** do dataset COCO, incluindo:

**Animais:**
- 🐱 Gato (cat)
- 🐶 Cachorro (dog)
- 🐴 Cavalo (horse)
- 🐑 Ovelha (sheep)
- 🐄 Vaca (cow)
- 🐘 Elefante (elephant)
- 🐻 Urso (bear)
- 🦒 Girafa (giraffe)

**Pessoas e Objetos:**
- 👤 Pessoa (person)
- 🚗 Carro (car)
- 🚲 Bicicleta (bicycle)
- 🏍️ Moto (motorcycle)
- 🛋️ Sofá (couch)
- 🪑 Cadeira (chair)
- 📱 Celular (cell phone)
- 💻 Laptop (laptop)

... e mais 62 classes.

### 🛠️ Tecnologias Utilizadas
ultralytics==8.0.0+  # YOLOv8
opencv-python==4.8.0+  # Processamento de imagem
numpy==1.24.0+  # Operações matemáticas
Pillow==10.0.0+  # Manipulação de imagens

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conexão com internet (primeira execução para baixar modelo)

### Instalação

#### 1. Clone o repositório

```bash
git clone https://github.com/hPedroSantos/classificao-cat-dog.git
cd classificao-cat-dog
```

#### 2. Instale as dependências

```bash
pip install ultralytics opencv-python
```

### Executando o Projeto C2

#### Opção A: Com imagens próprias

```bash
# 1. Baixar imagens de teste automaticamente
cd C2
python baixar_imagens.py

# 2. Executar o reconhecimento
python reconhecimento_yolo.py
```

#### Opção B: Com imagens da internet (sem download)

```bash
cd C2
python reconhecimento_yolo.py
```

O sistema automaticamente:
1. Carrega o modelo YOLOv8
2. Procura imagens em `imagens_teste/`
3. Se não encontrar, usa imagens de exemplo da internet
4. Detecta objetos
5. Salva resultados em `resultados/`

### Visualizar Resultados

Após a execução, os resultados estarão em:
C2/resultados/
├── detectado_gato_cachorro_01.jpg
├── detectado_cachorro_parque_01.jpg
└── ...

Abra as imagens para ver as **caixas delimitadoras** e **labels** dos objetos detectados.

---

## 📁 Estrutura do Projeto
classificao-cat-dog/
│
├── C1/                          # Projeto C1 (Classificação)
│   ├── modelo_classificacao.py
│   └── ...
│
├── C2/                          # Projeto C2 (Reconhecimento)
│   ├── reconhecimento_yolo.py   # Script principal
│   ├── baixar_imagens.py        # Download automático de imagens
│   │
│   ├── imagens_teste/           # Imagens para teste
│   │   ├── gato_cachorro_01.jpg
│   │   ├── cachorro_parque_01.jpg
│   │   └── ...
│   │
│   └── resultados/              # Resultados com detecções
│       ├── detectado_*.jpg
│       └── ...
│
└── README.md                    # Este arquivo

---

## 🎯 Funcionalidades do Sistema C2

### 1. Detecção Automática
- Identifica múltiplos objetos na mesma imagem
- Reconhece 80 classes diferentes

### 2. Localização Precisa
- Desenha caixas delimitadoras (bounding boxes)
- Mostra coordenadas exatas de cada objeto

### 3. Classificação com Confiança
- Exibe porcentagem de confiança de cada detecção
- Filtra detecções de baixa confiança

### 4. Processamento em Lote
- Processa múltiplas imagens automaticamente
- Gera estatísticas consolidadas

---

## 📊 Exemplo de Saída
============================================================
RECONHECEDOR DE OBJETOS - YOLOv8
Carregando modelo yolov8n.pt...
✓ Modelo carregado com sucesso!
[1/3] Processando: gato_cachorro_01.jpg
→ Resultado salvo: resultados/detectado_gato_cachorro_01.jpg
✓ Total detectado: 2 objeto(s)
Detecções:
- Cat: 1
- Dog: 1
Detalhes:
[1] CAT - 94.3%
[2] DOG - 91.7%

---

## 🎥 Demonstração

[Link do vídeo de demonstração será adicionado aqui]

---

## 📖 Referências

- **YOLOv8 Documentation**: https://docs.ultralytics.com/
- **COCO Dataset**: https://cocodataset.org/
- **Ultralytics GitHub**: https://github.com/ultralytics/ultralytics

---

## 📅 Histórico de Versões

- **v1.0** (Mai/2026) - C1: Classificação Binária (Gato vs Cachorro)
- **v2.0** (Mai/2026) - C2: Reconhecimento Multi-Objetos com YOLOv8