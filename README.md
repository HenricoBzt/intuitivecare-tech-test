# IntuitiveCare Tech Test - 


![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

API de Operadoras

Este projeto é uma solução para o teste técnico da **IntuitiveCare**, que consiste no desenvolvimento de uma API para buscar operadoras de planos de saúde ativas na ANS, além da criação de um frontend para consumir essa API.

## 🚀 Tecnologias Utilizadas

### Backend:
- **FastAPI** - Framework para construção da API
- **SQLAlchemy** - ORM para manipulação do banco de dados
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI para rodar a aplicação
- **Docker** *(opcional, ainda não implementado)*

### Frontend:
- **Vue.js** - Framework JavaScript para construção do frontend
- **Axios** - Cliente HTTP para consumir a API
- **Vite** - Ferramenta para build e desenvolvimento



## 🛠️ Como Rodar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/HenricoBzt/intuitivecare-tech-test.git
cd intuitivecare-tech-test/app/
```

### 2️⃣ Configurar o Backend

#### Criar e ativar um ambiente virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

#### Instalar as dependências
```bash
pip install -r backend/requirements.txt
```

#### Iniciar o servidor backend
```bash
cd backend
uvicorn main:app --reload
```
A API estará disponível em `http://localhost:8000`

---

### 3️⃣ Configurar o Frontend

#### Instalar as dependências
```bash
cd frontend
npm install
```

#### Rodar o frontend
```bash
npm run dev
```
O frontend estará disponível em `http://localhost:5173`

---

## 📦 Dockerização do Backend (Opcional)
Caso queira rodar o backend com Docker, crie um arquivo `Dockerfile` na pasta `backend/` com o seguinte conteúdo:

```dockerfile
# Dockerfile para FastAPI
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

Depois, rode os seguintes comandos:
```bash
docker build -t intuitivecare-backend .
docker run -p 8000:8000 intuitivecare-backend
```

---

 ## Web Scraping:  
   - Download automatizado de PDFs (Anexos I e II) do site da ANS.  
   - Compactação em arquivo ZIP.
   -
   ### RODAR O SCRIPT:
   ```bash
intuitive-tech-test/web_scraping/main.py
```
  

## Transformação de Dados**:  
   - Extração de tabelas de PDF para CSV.  
   - Tratamento de dados e normalização de colunas.
 ### RODAR O SCRIPT:
   ```bash
intuitive-tech-test/data_transform/main.py
```
  

## Banco de Dados:  
   - Modelagem de tabelas para operadoras e demonstrações contábeis.  
   - Queries analíticas para identificar maiores despesas.
 ### RODAR O SCRIPT:
   ```bash
intuitive-tech-test/database/main.py
```
  
---


---




💡 **Desenvolvido por [Henrico Bazante]** 🚀
