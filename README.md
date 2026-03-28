Sistema de Gestao Pet Shop
Projeto academico desenvolvido para a Faculdade Impacta, focado em uma arquitetura de 3 camadas (Full Stack) e metodologias ageis. O projeto pode ser executado em qualquer ambiente Python 3.10+, sendo recomendado o uso do PyCharm ou VS Code.

Funcionalidade Agil: Busca Dinamica
Seguindo os principios do Manifesto Agil, implementamos uma busca em tempo real que prioriza a interacao com o usuario e a entrega de valor. Esta funcao abrange as 3 camadas do projeto:

Front-end: Campo de pesquisa com evento onkeyup no arquivo pets.html para filtragem instantanea.

Back-end: Rota dedicada /pets/search/ no FastAPI para processamento logico do filtro.

Banco de Dados: Consulta otimizada com o operador ilike no PostgreSQL (Neon.tech), garantindo buscas flexiveis na nuvem.

Tecnologias
Front-end: HTML5, CSS3 e JavaScript.

Back-end: Python com framework FastAPI.

Banco de Dados: PostgreSQL hospedado no Neon.tech (SQLAlchemy ORM).

Como rodar o projeto
Instale as dependencias:
pip install fastapi sqlalchemy uvicorn psycopg2-binary

Entre na pasta do projeto:
cd Faculdade

Inicie o servidor:
uvicorn projeto_impacta:app --reload

Acesse o sistema: Abra o arquivo index.html no seu navegador.

Persistencia de Dados
Os dados estao sendo persistidos em uma instancia gerenciada de PostgreSQL no Neon.tech. Isso permite que a aplicacao seja testada sem a necessidade de um servidor de banco de dados local, garantindo que as informacoes do Pet Shop estejam sempre seguras e disponiveis na nuvem.