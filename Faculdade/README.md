# Sistema de Gestão Pet Shop

Projeto académico desenvolvido para a Faculdade Impacta, focado numa arquitetura de 3 camadas (Full Stack).

## Tecnologias

* **Front-end:** HTML5, CSS3 e JavaScript.
* **Back-end:** Python com framework FastAPI.
* **Banco de Dados:** PostgreSQL hospedado no Neon.tech (SQLAlchemy ORM).

## Como rodar o projeto

1. **Instale as dependências:**
   ```bash
   pip install fastapi sqlalchemy uvicorn psycopg2-binary
   
2. Entre na pasta do projeto:

cd Faculdade

3. Inicie o servidor:

uvicorn projeto_impacta:app --reload

4. Aceda ao sistema:
Abra o ficheiro index.html no seu navegador.

### Persistência de Dados
Os dados estão sendo persistidos em uma instância gerenciada de PostgreSQL no Neon.tech. 
Isso permite que a aplicação seja testada sem a necessidade de um servidor de banco de dados local.
