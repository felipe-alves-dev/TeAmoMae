# Especificação de Requisitos

| [Introdução](https://github.com/felipe-alves-dev/TeAmoMae) | Especificação de Requisitos |
| ---------------------------------------------------------- | --------------------------- |

## Requisitos Não-Funcionais

### RNF 01

Deve rodar na World Wide Web.

### RNF 02

Deve utilizar as linguagens: HTML, CSS, JavaSCript e Python.

### RNF 03

Deve utilizar o micro-framework Flask.

### RNF 04

Deve ter todas as páginas responsivas.

### RNF 05

Deve armazenar os dados persistentes em um banco de dados relacional.

### RNF 06

Deve armazenar os id's dos usuários e dos meses como um UUID aleatório ao invés
de números crescentes.

### RNF 07

Deve gravar/trafegar a senha do usuário utilizando-se o algoritmo bcrypt para
criptografia.

### RNF 08

Deve ficar fora do ar caso haja ineficácia, voltando apenas ao ser consertado.

## Requisitos Funcionais

### RF 01

O sistema deve permitir que o usuário entre em sua conta.

- O formulário deve possuir os campos: _email_ e _senha_.
- O campo _email_ deve permitir o mínimo de 6 e o máximo de 254 caracteres.
- O campo _senha_ deve permitir o mínimo de 8 e o máximo de 32 caracteres.
- Os campos do formulário devem ser obrigatórios.
- Os campos com dados inválidos devem ser destacados.
- Os toasts devem ser exibidos nas tentativas mal sucedidas.
- O usuário deve ser redirecionado para o painel caso a tentativa seja bem
  sucedida.

### RF 02

O sistema deve permitir que o usuário crie uma conta.

- O formulário deve possuir os campos: _email_, _senha_ e _confirmar senha_.
- O campo _email_ deve permitir o mínimo de 6 e o máximo de 254 caracteres.
- O campo _senha_ deve permitir o mínimo de 8 e o máximo de 32 caracteres.
- O campo _confirmar senha_ deve permitir o mínimo de 8 e o máximo de 32
  caracteres.
- Os campos do formulário devem ser obrigatórios.
- Os toasts devem ser exibidos nas tentativas bem e mal sucedidas.
- O usuário deve ser redirecionado para a página de login caso a tentativa seja
  bem sucedida.

### RF 03

O sistema deve permitir que o usuário adicione peças no mês.

- O formulário deve possuir os campos: _nome_, _pedras_, _feitas_ e
  _valor_.
- O campo _nome_ deve permitir o mínimo de 2 e o máximo de 32 caracteres.
- O campo _pedras_ deve limitar o número para o mínimo de 1 e o máximo de 400.
- O campo _feitas_ deve limitar o número para o mínimo de 1 e o máximo de 300.
- O campo _valor_ deve aceitar apenas os valores "0.025" e "0.040".
- Os campos do formulário devem ser obrigatórios.
- Os toasts devem ser exibidos nas tentativas bem e mal sucedidas.
- O usuário deve ser redirecionado para o painel nas tentativas bem e mal
  sucedidas.

### RF 04

O sistema deve listar todas as peças adicionadas no mês.

- Os dados devem ser: _data de cadastro_, _nome_, _pedras_, _valor_,
  _qtd de peças feitas_, _qtd de pedras feitas_ e _lucro_.

### RF 05

O sistema deve permitir que o usuário remova peças que estão adicionadas no
mês.

- O usuário deve ser consultado com uma confirmação antes da remoção.
- Os toasts devem ser exibidos nas tentativas bem e mal sucedidas.
- O usuário deve ser redirecionado para o painel nas tentativas bem e mal
  sucedidas.

### RF 06

O sistema deve exibir o resumo do mês.

- Os dados devem ser: _mês_, _total de peças_, _total de pedras_ e _lucro_.

### RF 07

O sistema deve permitir que o usuário encerre o mês.

- O usuário deve ser consultado com uma confirmação antes do encerramento.
- O novo mês do usuário deve ser o mês atual do servidor caso ele seja
  encerrado do dia 1 ao dia 5.
- O novo mês do usuário deve ser o mês seguinte do servidor caso ele seja
  encerrado antes do dia 1 e depois do dia 5.
- O usuário não pode ter permissão de encerrar o mês caso o mês do usuário seja
  o mês seguinte do servidor.
- Os toasts devem ser exibidos nas tentativas bem e mal sucedidas.
- O usuário deve ser redirecionado para o painel nas tentativas bem e mal
  sucedidas.

### RF 08

O sistema deve permitir que o usuário compartilhe seus meses com outras
pessoas.

- A página de compartilhamento deve exibir todos os meses do usuário.
- Ao clicar sobre um mês, deve-se abrir uma página seguindo os requisitos
  _RF 04_ e _RF 06_.
- O usuário deve ter a possibilidade de copiar o link de sua página de
  compartilhamento.
