# trybe-crawling-examples
Repositório com exemplos de raspagem de dados usando python sem bibliotecas especificas para isso.

## Introdução
Esse repositório foi criado para apresentar exemplos do que é possível fazer através de raspagem de dados.

## Dependências
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Python 3+](https://www.python.org/downloads/)

## Get started

1 - Clone o repositório com o comando e abra a pasta com o VSCode: 

```bash
git clone https://github.com/leandroluk/trybe-crawling-examples
```

2 - Pelo terminal da IDE, inicialize o ambiente virtual do python utilizando o comando:

```bash
# dependendo do seu sistema operacional o executavel do python pode variar
# e precisamos utilizar o python 3
python -m venv venv
# ou
python3 -m venv venv
```

3 - Dependendo do seu sistema operacional inicialize o ambiente de desenvolvimento conforme os comandos abaixo:

```bash
# Para Windows (utilizando o cmd): 
.\venv\Scripts\activate
# Para Linux ou Macos (utilizando o bash ou sh):
source ./venv/bin/activate
```

4 - Faça a atualização e instalação das dependências do projeto com o comando:

```bash
pip3 install --upgrade pip setuptools && pip3 install -r requirements.txt
```

## Rodando alguns crawlers

Esse repositório foi preparado pra permitir a criação de crawlers que utilizam as bibliotecas mais usadas para raspagem de dados: `requests` e `selenium`. Pra cada situação você pode utilizar uma ou as duas com base no fluxo a ser feito.

Abaixo estão os mini-projetos desenvolvidos:

- **src.selenium.betrybe.fetch_course_content**: Acessa o curso da trybe e extrai os link's de acesso aos conteúdos. Para funcionar é necessário definir as variaveis de ambiente `TRYBE_USER` e `TRYBE_PASS`. Você também pode definí-las em um arquivo na pasta raiz chamado ".env" e então executar o código.