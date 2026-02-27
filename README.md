# Organize-but-python

Ferramenta CLI e GUI para organizar arquivos baseado na extensão do arquivo.

## Funcionalidades

- Organiza arquivos por tipo (vídeos, imagens, dev, documentos, etc.)
- Suporte a extensões compostas (ex: .tar.gz)
- Trata arquivos sem extensão
- Interface simples via terminal e GUI

## Instalação

Clone o repositório:

<p>
  <code>git clone https://github.com/ErikTatsuya/Organize-but-python/ && cd organize</code>
</p>

Instale localmente:

<p>
	<code>pip install .</code>
</p>

Ou instale em modo desenvolvimento:

<p>
	<code>pip install -e .</code>
</p>

## Uso

organize <opção> <caminho>

Exemplo:

<p>
	<code>organize run ~/Dowloads</code>
</p>

ou

<p>
	<code>organize gui</code>
</p>

## Como funciona

O algoritmo:

1. Verifica primeiro extensões compostas (ex: .tar.gz)
2. Verifica se o arquivo não possui extensão
3. Identifica a categoria da extensão
4. Move o arquivo para o diretório correspondente

## Licença

MIT

# Organize-but-python
