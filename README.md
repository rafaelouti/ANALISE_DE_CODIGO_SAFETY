# Code Analyzer

**Code Analyzer** é uma aplicação simples que oferece análise de código para identificar possíveis problemas de segurança, performance e boas práticas. Ele foi projetado para realizar consultoria de código automaticamente, com foco em sugestões de melhorias para código Python.

## Funcionalidades

- Detecta problemas de segurança, como o uso de funções perigosas (`eval()`).
- Sinaliza ineficiências de performance, como loops aninhados.
- Oferece sugestões de melhorias de boas práticas, como verificação de variáveis `None`.
- Interface simples para enviar o código e receber a análise em tempo real.

## Como funciona

1. O usuário envia um trecho de código Python através de um formulário.
2. O código é processado e analisado pelo **Code Analyzer**.
3. Um relatório é gerado, identificando possíveis problemas e fornecendo sugestões de melhorias.

## Tecnologias utilizadas

- **Python**: Linguagem base da aplicação.
- **Bottle**: Framework web leve utilizado para criar a API e a interface web.
- **HTML/CSS**: Para a interface básica do usuário.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/code-analyzer.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd code-analyzer
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Execute a aplicação:

    ```bash
    python app.py
    ```

6. Acesse a aplicação no navegador:

    ```
    http://localhost:8080
    ```

## Como usar

1. Após iniciar o servidor, abra o navegador e vá para `http://localhost:8080`.
2. Cole o código que deseja analisar na caixa de texto e clique em "Enviar".
3. A aplicação analisará o código e exibirá os resultados com sugestões de melhorias.

## Exemplo de Código

Este é um exemplo de código que pode ser analisado pelo **Code Analyzer**:

```python
def unsafe_function(input_data):
    result = eval(input_data)  # Uso perigoso de eval
    return result
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.


### Personalize as seções:
- **"Tecnologias utilizadas"**: Liste as bibliotecas e ferramentas que você usou no seu projeto.
- **"Exemplo de Código"**: Você pode alterar ou adicionar mais exemplos de código que sua aplicação analisa.
- **"Contribuições"**: Defina se aceita contribuições e descreva o processo, se desejar.

!
