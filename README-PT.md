# Statistics
## Calculadora de Alta Precisão por Kenielf
![janela cheia](https://github.com/kenielf/statistics/blob/main/img/full_window.png?raw=true)

# [ENGLISH HERE](README.md)

# Instalação
Requer Python3.X

# Instalação Linux:
```bash
$ git clone https://github.com/kenielf/statistics
$ cd statistics/source
$ python3 -m venv env
$ source ./env/bin/activate
$ python3 -m pip install -r ../requirements.txt
```

# Instalação Windows:
Baixe e extraia o lançamento mais recente
```
cd \statistics-main\source
python -m venv env
env\Scripts\activate.bat
python -m pip install -r ..\requirements.txt
```
Usuários no Windows podem simplesmente baixar o lançamento mais recente, descomprimir e rodar o statcalc.exe

Para executar o programa, use o comando `python3 statcalc.py` dentro do diretório que contém `statcalc.py`

# Uso
Execute o programa normalmente, ou passe os argumentos `-t` ou `--terminal` para forçar output no terminal.
![janela terminal](https://github.com/kenielf/statistics/blob/main/img/terminal_window.png?raw=true)
Mais informações em `--help`

# A FAZER
 - [X] Suporte para SYSARGS;
 - [X] Melhorar Cálculos;
 - [X] Adicionar Suporte para Windows;
 - [X] Adicionar Interface Gráfica;
 - [X] Refatorar o código para melhor legibilidade e facilidade de futuras refatorações;
 - [ ] Adicionar função para salvar como HTML;
 - [ ] Adicionar função para ler arquivos HTML;

# Possíveis Futuras Adições
 - [ ] Suporte CLI NCurses para Usabilidade;
 - [X] Seleção de Entradas Seletivas;
 - [ ] Função Get from Table;
 - [ ] Suporte SQL;

# LICENÇA
Copyright (c) 2021 Chrystian Franklin. This project is [MIT](https://github.com/kenielf/statistics/blob/main/LICENSE) licensed.
