# Sistema de Gestão Pet Shop

Projeto acadêmico desenvolvido para a **Faculdade Impacta**, focado em uma arquitetura de **3 camadas (Full Stack)** e metodologias ágeis. O projeto utiliza persistência em nuvem e foi atualizado para suportar agendamentos e controles dinâmicos de saúde.

## Funcionalidades Ágeis e 3 Camadas

O projeto foi construído seguindo os pilares do **Manifesto Ágil**, priorizando a interação com o usuário, respostas rápidas a mudanças e entrega contínua de software funcional.

### 1. Busca Dinâmica (Real-time)
Permite a filtragem instantânea de registros sem a necessidade de recarregar a página.
* **Front-end**: Evento `onkeyup` no arquivo `pets.html` para filtragem via JavaScript.
* **Back-end**: Endpoint `/pets/search/` processando filtros lógicos no FastAPI.
* **Banco de Dados**: Consulta com operador `ilike` no PostgreSQL (**Neon.tech**).

### 2. Agendamento de Tosa (Feature Opcional)
Implementação de controle de datas para serviços, integrada de forma flexível para não bloquear o fluxo do usuário.
* **Front-end**: Input do tipo `date` no `index.html` e exibição formatada na lista.
* **Back-end**: Evolução das rotas de `POST` e `PUT` para persistência do atributo de forma opcional (`None`).
* **Banco de Dados**: Atualização do Schema para inclusão da coluna `data_tosa` aceitando valores nulos (`nullable=True`).

### 3. Controle de Vacinação (Nova Feature de Saúde)
Nova funcionalidade que agrega valor imediato ao gerenciamento do pet, controlando o status vacinal.
* **Front-end**: Elemento de seleção (`select`) no formulário e renderização de tags visuais dinâmicas (vermelho/verde) na listagem.
* **Back-end**: Regra de negócio integrada às rotas principais mapeando o payload de dados.
* **Banco de Dados**: Evolução do Schema com a coluna `vacinado` para persistência em nuvem.

## Tecnologias
* **Front-end**: HTML5, CSS3 (com Backdrop-filter para efeito Glassmorphism) e JavaScript Vanilla.
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
Os dados estão sendo persistidos em uma instância gerenciada de **PostgreSQL no Neon.tech**. Isso garante que a aplicação funcione com persistência real na nuvem, permitindo que as informações do Pet Shop estejam sempre seguras, disponíveis e tratadas corretamente nas 3 camadas.