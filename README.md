# Projeto de Web Scraping com Alerta de Preço

Este projeto utiliza **BeautifulSoup** para realizar *web scraping* de um produto específico e armazena as informações de preço coletadas em um banco de dados **SQLite**. Caso o preço atual seja menor que o menor valor registrado na base de dados, um bot envia uma mensagem no **Telegram** notificando sobre o menor preço encontrado.

---

## Funcionalidades

- **Web Scraping com BeautifulSoup**: Realiza a extração de informações de preço de um produto em um site específico.
- **Armazenamento em SQLite**: As leituras de preço são armazenadas em um banco de dados SQLite para histórico e comparação.
- **Notificação no Telegram**: Se o preço lido for menor que o menor valor já registrado, um bot do Telegram envia uma mensagem de alerta.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Gerenciador de Pacotes**: Poetry
- **Bibliotecas Principais**:
  - `BeautifulSoup`: Para realizar *web scraping*.
  - `sqlite3`: Para o armazenamento dos preços em um banco de dados local.
  - `python-telegram-bot`: Para enviar notificações no Telegram.

---

## Configuração e Uso

### 1. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

### 2. Instalar Dependências

Utilize o **Poetry** para gerenciar as dependências do projeto:

```bash
poetry install
```

### 3. Configurar o Bot do Telegram

- Crie um bot no Telegram usando o [BotFather](https://core.telegram.org/bots#botfather).
- Obtenha o *Token* do bot e o *Chat ID* do usuário ou grupo onde deseja enviar as notificações.
- Configure essas informações em um arquivo `.env` ou diretamente no script.

### 4. Executar o Script

Ative o ambiente virtual do Poetry e execute o script:

```bash
poetry shell
poetry run python app.py
```

---

## Como Funciona

1. O script realiza o *web scraping* do produto usando **BeautifulSoup**.
2. Os dados coletados (incluindo o preço e a data da coleta) são armazenados no **SQLite**.
3. Antes de salvar o novo valor, o script verifica se o preço atual é o menor valor já registrado:
   - Se for, o **bot do Telegram** envia uma notificação alertando sobre o novo menor preço.
   - Caso contrário, os dados são apenas armazenados sem enviar notificação.

---

## Customização

- **Modificar o Site de Scraping**: O script pode ser facilmente adaptado para realizar *web scraping* de outros sites. Basta ajustar a URL e os seletores CSS utilizados.
- **Configuração de Alertas**: Você pode personalizar a mensagem e o comportamento do bot no Telegram de acordo com suas preferências.

---

## Requisitos do Sistema

- Python 3.11 ou superior
- Poetry
- Conexão ativa com a internet para realizar o *web scraping* e enviar notificações no Telegram.

---

## Futuras Melhorias

- **Deploy em uma Máquina Virtual na Cloud**: Implementar o projeto em uma máquina virtual em provedores de nuvem como AWS, Azure ou Google Cloud para que o *scraper* possa funcionar de forma contínua e automática, sem a necessidade de execução manual.
- **Monitoramento de Vários Itens**: Expandir o bot para coletar informações de vários produtos diferentes, permitindo que os usuários sejam notificados sobre preços reduzidos em uma lista personalizada de itens.
- **Melhorias na Persistência dos Dados**: Considerar o uso de um banco de dados mais robusto, como PostgreSQL, se o volume de dados aumentar significativamente.
