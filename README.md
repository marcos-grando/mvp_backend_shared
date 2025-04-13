### Desenvolvimento Full Stack - PUC-Rio

## MVP Back End com Flask + Interface React:
# 🛒 Big Loja (loja virtual) 

O objetivo do MVP foi desenvolver uma loja virtual, contemplando tanto a experiência do usuário quanto o gerenciamento administrativo do sistema. 

👤 Usuário: pode navegar entre produtos, filtrar por categoria ou preço, adicionar e manipular itens no carrinho, finalizar compras e acompanhar pedidos no histórico.

🛠️ Administrador: conta com um painel de controle que permite o cadastro e gerenciamento de produtos e categorias, além de visualizar todos os pedidos realizados (incluindo a opção de cancelamento de pedidos).istrador: conta com um painel de controle que permite o cadastro e gerenciamento de produtos e categorias, além de visualizar todos os pedidos realizados (incluindo a opção de cancelamento de pedidos).

---

## 🧩 Módulo Auxiliar Compartilhado (backend_shared)

Esse repositório **não é um container separado**, mas é uma parte essencial do sistema. Ele serve como base para os outros backends, contendo arquivos e pastas que são utilizados por todos eles. Aqui ficam o banco de dados, as configurações da aplicação e as pastas de imagens.

---

## 📂 O que tem aqui dentro

- 🗃️ `database.db` – banco de dados SQLite que armazena tudo do sistema (produtos, categorias, compras, etc)
- ⚙️ `config.py` – configurações compartilhadas (como conexão com o banco)
- 📁 `uploads/` – onde são salvas as imagens dos produtos
- 📁 `imgs_compras/` – onde são salvas as imagens vinculadas aos pedidos realizados

---

## 🔗 Usado por:

- [`backend_produtos`](https://github.com/marcos-grando/mvp_backend_produtos): banco de dados + pasta `uploads/`
- [`backend_categorias`](https://github.com/marcos-grando/mvp_backend_categorias): apenas o banco de dados
- [`backend_compras`](https://github.com/marcos-grando/mvp_backend_compras): banco de dados + `uploads/` + `imgs_compras/`

Cada um desses containers monta esse diretório como volume, pra poder acessar os mesmos dados, imagens e estrutura de banco.

---

## ❗ Importante

Esse diretório **não é um container**.  
Ele só precisa estar presente na mesma pasta dos outros repositórios quando você rodar o `docker-compose`.

### Estrutura do sistema:

- 🌐 **API externa**: [FakeStore](https://fakestoreapi.com/) → usada para popular a base com produtos fictícios. O modelo `Produto` foi estruturado com base nos dados dessa API (nome, valor, imagem, etc).
- 🔹 [`backend_categorias`](https://github.com/marcos-grando/mvp_backend_categorias) → responsável pelo cadastro e gerenciamento das categorias dos produtos
- 🔹 [`backend_produtos`](https://github.com/marcos-grando/mvp_backend_produtos) → responsável pelo gerenciamento dos produtos (incluindo uploads das imagens dos produtos)
- 🔹 [`backend_compras`](https://github.com/marcos-grando/mvp_backend_compras) → responsável por registrar e consultar compras feitas na loja
- 🔸 [`backend_shared`] ← Você está nesse repositório
- 💠 [`frontend`](https://github.com/marcos-grando/mvp_frontend_bigloja) → interface React responsável pela exibição dos produtos, carrinho, compras e painel administrativo, conectando-se às APIs

***OBS: `docker-compose`***  
 - O sistema utiliza 3 APIs diferentes, com dependências entre os módulos  
 - Por isso, é recomendado utilizar o `docker-compose`, que está no repositório `frontend`  
 - Isso evita a necessidade de buildar e subir manualmente cada componente um por um

---

### ▶️ Passo a passo

1. Tenha o **Docker** instalado na máquina
2. Clone todos os repositórios acima na mesma pasta
3. No terminal, execute:

```bash
docker-compose up --build
```

---

## 🧠 Observações
Esse repositório faz parte de um MVP acadêmico. O sistema foi dividido em partes que se comunicam entre si por rotas. O backend foi feito com Flask (Python) e frontend com React.js.

### 🙋‍♂️ Autor
Desenvolvido por Marcos Grando ✌️

"""
