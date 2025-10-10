# trab-escola-api
API desenvolvida com Flask, seguindo o padrão MVC para uma arquitetura limpa e escalável. O projeto oferece endpoints para o gerenciamento de professores, turmas e alunos, com suporte a Docker para fácil implantação e portabilidade. 
Idealizado por Gabriel Bezerra Ledezma, Guilherme de Souza Ferraz e Felipe Batista de Oliveira Nascimento, com o suporte  de Paulo Augusto de Moura Neto.
# Escola API - Guia de Instalação Simples

Uma API para gerenciar professores, turmas e alunos de forma fácil e organizada.

## OPÇÃO 1: Com Docker (O MAIS FÁCIL!)
Primeiro, instale o Docker:
https://www.docker.com/products/docker-desktop/

Baixe e instale o Docker Desktop para Windows ou Mac. Reinicie o computador se solicitado.

Passos:
1. Abra o Prompt de Comando (Windows: Windows + R, digite `cmd` e Enter) ou o Terminal (macOS).
2. Vá até a pasta do projeto:
```bash
cd C:\caminho\para\sua\pasta\EXPLORER
```
Dica: digite `cd` e arraste a pasta para o terminal.

3. Execute:
```bash
docker-compose up -d
```

4. Aguarde a configuração (pode demorar alguns minutos na primeira vez).

5. Teste:
Abra o navegador em: http://localhost:5000

Para parar a API:
```bash
docker-compose down
```

## OPÇÃO 2: Sem Docker
Primeiro, instale o Python (3.8 ou superior):
https://www.python.org/downloads/

IMPORTANTE: marque "Add Python to PATH" durante a instalação no Windows.

Passos:
1. Abra o Prompt de Comando/Terminal.
2. Vá até a pasta do projeto:
```bash
cd C:\caminho\para\sua\pasta\EXPLORER
```
3. Crie um ambiente virtual:
```bash
python -m venv venv
```
4. Ative o ambiente virtual:
- No Windows:
```bash
venv\Scripts\activate
```
- No macOS / Linux:
```bash
source venv/bin/activate
```
Quando ativado, verá `(venv)` no início da linha.

5. Instale dependências:
```bash
pip install -r requirements.txt
```

6. Configure o banco de dados:
```bash
flask db init
flask db migrate
flask db upgrade
```

7. Rode a API:
```bash
flask run
```

8. Mensagem esperada:
```
Running on http://127.0.0.1:5000
```
Abra: http://localhost:5000

Para parar a API: pressione Ctrl + C no terminal.

