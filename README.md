# 🐾 PawVision — Classificador Gato vs Cachorro

![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-FF6F00?style=flat&logo=tensorflow&logoColor=white)
![Teachable Machine](https://img.shields.io/badge/Teachable%20Machine-4285F4?style=flat&logo=google&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)

Aplicação web de visão computacional que classifica imagens como **Gato** ou **Cachorro** em tempo real usando um modelo treinado no Google Teachable Machine e executado localmente via TensorFlow.js.

---

## 📋 Sobre o Projeto

Trabalho da disciplina de Inteligência Artificial — implementação completa de um pipeline de Machine Learning: coleta de dados → treinamento → aplicação web → avaliação.

**Arquitetura do modelo:** Transfer Learning com MobileNet (pré-treinado no ImageNet). O Teachable Machine retreina apenas as camadas finais da rede com o dataset personalizado de gatos e cachorros.

---

## 🗂️ Estrutura do Repositório

```
cat-dog-classifier/
│
├── index.html              # Aplicação web principal
├── server.py               # Servidor local Python (HTTP simples)
├── README.md               # Este arquivo
│
├── my_model/               # Arquivos do modelo exportado (Teachable Machine)
│   ├── model.json          # Arquitetura + referência dos pesos
│   ├── weights.bin         # Pesos treinados da rede neural
│   └── metadata.json       # Nomes das classes e configurações
│
├── dataset/                # Dataset organizado por classe
│   ├── cat/                # Imagens de gatos (treino)
│   └── dog/                # Imagens de cachorros (treino)
```

---

## ⚙️ Como Executar Localmente

> **Importante:** A aplicação **não pode** ser aberta diretamente como arquivo (`file://`). O TensorFlow.js precisa de um servidor HTTP para carregar os pesos do modelo.

### Opção 1 — Python (recomendado)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/cat-dog-classifier.git
cd cat-dog-classifier

# Inicie o servidor
python server.py

# Acesse no navegador
# http://localhost:8000
```

### Opção 2 — VS Code Live Server

Instale a extensão **Live Server** e clique em "Go Live" com o `index.html` aberto.

### Opção 3 — Node.js

```bash
npx serve .
```

---

## 🧠 Como Usar a Aplicação

1. **Carregue uma imagem** — arraste ou clique na área de upload
2. **Veja a predição** — o modelo exibe a classe e a confiança em tempo real
3. **Registre o resultado** — selecione a classe real e clique em "Registrar"
4. **Avalie o modelo** — a matriz de confusão e métricas são geradas automaticamente

---

## 📊 Métricas de Avaliação

A aplicação calcula automaticamente:

| Métrica | Fórmula | O que mede |
|---------|---------|-----------|
| **Acurácia** | (TP + TN) / Total | % geral de acertos |
| **Precisão** | TP / (TP + FP) | Qualidade das predições positivas |
| **Recall** | TP / (TP + FN) | Capacidade de encontrar todos os positivos |
| **F1-Score** | 2 × (P × R) / (P + R) | Balanço entre Precisão e Recall |

> **Convenção:** Gato = classe positiva, Cachorro = classe negativa.

---

## 🏗️ Tecnologias

- **Google Teachable Machine** — Treinamento do modelo (transfer learning com MobileNet)
- **TensorFlow.js** — Inferência no browser, sem backend
- **HTML5 / CSS3 / JavaScript** — Interface web
- **Python** — Servidor de desenvolvimento
