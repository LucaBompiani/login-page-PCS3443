# Atividade1 - Sistema de Autenticação de Usuários

Um sistema simples de autenticação de usuários baseado em FastAPI com interface web.

Desenvolvido por Luca Bompiani e João Luiz Giglio Laudissi

## Funcionalidades

- Cadastro e login de usuários
- Autenticação baseada em tokens JWT
- Hash de senhas com bcrypt
- Banco de dados PostgreSQL
- Containerização com Docker
- Interface web frontend

## Início Rápido

### Pré-requisitos

- Docker e Docker Compose
- Make (opcional, para facilitar o gerenciamento)

### Executando o Sistema

```bash
# Usando Make (recomendado)
make run

# Ou manualmente
sudo docker-compose build --no-cache
sudo docker-compose up -d
```

O sistema estará disponível em: http://localhost:8000

### Outros Comandos

```bash
# Ver logs em tempo real
make logs

# Parar e limpar tudo
make clean

# Verificar se o sistema está funcionando
make health

# Mostrar ajuda
make help
```

## Como Usar

1. **Acesse a aplicação**: Abra http://localhost:8000 no seu navegador
2. **Cadastre um novo usuário**: Clique em "Cadastrar" e preencha o formulário
3. **Faça login**: Use suas credenciais para entrar
4. **Dashboard**: Após o login, você verá suas informações de usuário

## Endpoints da API

- `POST /api/v1/users/` - Cadastrar um novo usuário
- `POST /api/v1/auth/token` - Fazer login e obter token de acesso
- `GET /` - Servir a interface web frontend

## Estrutura do Projeto

```
├── app/                 # Aplicação FastAPI
│   ├── api/v1/         # Endpoints da API
│   ├── core/           # Configuração e segurança
│   ├── db/             # Configuração do banco de dados
│   ├── schemas/        # Modelos Pydantic
│   └── services/       # Lógica de negócio
├── frontend/           # Interface web
├── docker-compose.yml  # Serviços Docker
├── Dockerfile         # Container da aplicação
└── Makefile           # Comandos de gerenciamento
```

## Desenvolvimento

O sistema utiliza:
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: HTML/CSS/JavaScript vanilla
- **Autenticação**: Tokens JWT com hash de senhas bcrypt
- **Containerização**: Docker com Docker Compose
