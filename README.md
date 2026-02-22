# Organize-but-python

Ferramenta de linha de comando para organizar arquivos por categoria.

## Funcionalidades

- Organiza arquivos por tipo (vídeos, imagens, dev, documentos, etc.)
- Suporte a extensões compostas (ex: .tar.gz)
- Trata arquivos sem extensão
- Interface simples via terminal

## Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/Organize-but-python.git
cd organize

Instale localmente:

pip install .

Ou instale em modo desenvolvimento:

pip install -e .

## Uso

organize CAMINHO

Exemplo:

organize .

## Como funciona

O algoritmo:

1. Verifica primeiro extensões compostas (ex: .tar.gz)
2. Verifica se o arquivo não possui extensão
3. Identifica a categoria da extensão
4. Move o arquivo para o diretório correspondente

## Licença

MIT
# Organize-but-python
