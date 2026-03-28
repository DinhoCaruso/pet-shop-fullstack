# Sistema de Gestão Pet Shop

Projeto acadêmico desenvolvido para a **Faculdade Impacta**, focado em uma arquitetura de **3 camadas (Full Stack)** e metodologias ágeis. O projeto pode ser executado em qualquer ambiente Python 3.10+, sendo recomendado o uso do PyCharm ou VS Code.

## Funcionalidade Ágil: Busca Dinâmica
Seguindo os princípios do **Manifesto Ágil**, implementamos uma busca em tempo real que prioriza a interação com o usuário e a entrega de valor. Esta função abrange as 3 camadas do projeto:

* **Front-end**: Campo de pesquisa com evento **onkeyup** no arquivo `pets.html` para filtragem instantânea.
* **Back-end**: Rota dedicada **/pets/search/** no FastAPI para processamento lógico do filtro.
* **Banco de Dados**: Consulta otimizada com o operador **ilike** no PostgreSQL (**Neon.tech**), garantindo buscas flexíveis na nuvem.

## Tecnologias
* **Front-end**: HTML5, CSS3 e JavaScript.
* **Back-end**: Python com framework FastAPI.
* **Banco de Dados**: PostgreSQL hospedado no Neon.tech (SQLAlchemy ORM).

## Como rodar o projeto
1. **Instale as dependências**:
   `pip install fastapi sqlalchemy uvicorn psycopg2-binary`
2. **Entre na pasta do projeto**:
   `cd Faculdade`
3. **Inicie o servidor**:
   `uvicorn projeto_impacta:app --reload`
4. **Acesse o sistema**: Abra o arquivo `index.html` no seu navegador.

## Persistência de Dados
Os dados estão sendo persistidos em uma instância gerenciada de **PostgreSQL no Neon.tech**. Isso permite que a aplicação seja testada sem a necessidade de um servidor de banco de dados local, garantindo que as informações do Pet Shop estejam sempre seguras e disponíveis na nuvem.