# Calculadora em Python 🧮

## Sobre o projeto

Este é um projeto pessoal desenvolvido em Python com o objetivo de praticar lógica de programação e criar uma calculadora simples pelo terminal.

O programa permite que o usuário informe dois números, escolha uma operação matemática e veja o resultado. Também é possível realizar novas operações sem precisar reiniciar o programa.

## Tecnologias utilizadas

- **Python 3**
- **Terminal/console** para interação com o usuário

## Funcionalidades

A calculadora oferece cinco operações:

1. Adição (+)
2. Subtração (-)
3. Multiplicação (×)
4. Divisão (/)
5. Resto da divisão (%)

O programa também verifica se a opção escolhida está entre as operações disponíveis e permite continuar calculando até o usuário digitar `exit`.

## Conceitos de programação praticados

- Variáveis para armazenar os números, a opção escolhida e o resultado.
- `input()` para receber informações do usuário.
- `float()` e `int()` para converter os dados digitados.
- Lista para armazenar as opções válidas.
- Estrutura `while` para repetir a calculadora.
- Estruturas condicionais `if`, `elif` e `else` para selecionar a operação.
- Operadores aritméticos: `+`, `-`, `*`, `/` e `%`.
- F-strings para mostrar os resultados de forma dinâmica.

## Como executar

1. Instale o [Python](https://www.python.org/downloads/), caso ainda não esteja instalado.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute o arquivo Python. Por exemplo:

   ```bash
   python calculadora.py
   ```

   Se o comando `python` não funcionar no Windows, tente:

   ```bash
   py calculadora.py
   ```

## Exemplo de uso

```text
digite um numero: 10
digite outro numero: 5

ESCOLHA A FORMULA DA SOMA
1 = mais
2 = menos
3 = vezes
4 = dividido
5 = resto da divizao

digite o numero da opçao: 3
o numero 10.0 x o numero 5.0 e igual a 50.0
```

## Próximas melhorias

- Tratar a divisão por zero.
- Melhorar as mensagens e a validação das entradas.
- Permitir que o usuário escolha sair digitando `exit` de forma mais intuitiva.
- Organizar o código em funções para facilitar a manutenção.

## Autor

Projeto pessoal desenvolvido para praticar Python e evoluir na área de programação.
