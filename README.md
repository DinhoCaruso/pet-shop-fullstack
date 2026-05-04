# Sistema de Gestão Pet Shop

Projeto acadêmico desenvolvido para a **Faculdade Impacta**, focado em uma arquitetura de **3 camadas (Full Stack)** e metodologias ágeis. O projeto utiliza persistência em nuvem e foi atualizado para suportar agendamentos dinâmicos.

## Funcionalidades Ágeis e 3 Camadas

O projeto foi construído seguindo os pilares do **Manifesto Ágil**, priorizando a interação com o usuário e a resposta rápida a mudanças.

### 1. Busca Dinâmica (Real-time)
Permite a filtragem instantânea de registros sem a necessidade de recarregar a página.
* **Front-end**: Evento `onkeyup` no arquivo `pets.html` para filtragem via JavaScript.
* **Back-end**: Endpoint `/pets/search/` processando filtros lógicos no FastAPI.
* **Banco de Dados**: Consulta com operador `ilike` no PostgreSQL (**Neon.tech**).

### 2. Agendamento de Tosa (Nova Feature)
Implementação de controle de datas para serviços, integrando todo o ecossistema do software.
* **Front-end**: Input do tipo `date` no `index.html` e exibição formatada com ícones informativos na lista.
* **Back-end**: Evolução das rotas de `POST` e `PUT` para persistência do novo atributo.
* **Banco de Dados**: Atualização do Schema (Schema Evolution) para inclusão da coluna `data_tosa`.

## Tecnologias
* **Front-end**: HTML5, CSS3 (com Backdrop-filter) e JavaScript.
* **Back-end**: Python com framework FastAPI.
* **Banco de Dados**: PostgreSQL hospedado no Neon.tech com SQLAlchemy ORM.

## Como rodar o projeto
1. **Instale as dependências**:
   `pip install fastapi sqlalchemy uvicorn psycopg2-binary`
2. **Entre na pasta do projeto**:
   `cd Faculdade`
3. **Inicie o servidor**:
   `uvicorn projeto_impacta:app --reload`
4. **Acesse o sistema**: Abra o arquivo `index.html` no seu navegador.

## Persistência de Dados
Os dados estão sendo persistidos em uma instância gerenciada de **PostgreSQL no Neon.tech**. Isso garante que a aplicação seja testada com persistência real na nuvem, permitindo que as informações do Pet Shop estejam sempre seguras e disponíveis.