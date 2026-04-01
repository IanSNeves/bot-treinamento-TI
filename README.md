## Sistema de Autenticação (Login)

O projeto possui um sistema de autenticação de usuários para proteger o acesso à interface principal do assistente.

### Tecnologias Utilizadas

* **Flask-Login:** Gerenciamento de sessões de usuário, controlando quem está logado e protegendo rotas específicas.
* **Flask-SQLAlchemy:** Mapeamento objeto-relacional (ORM) para comunicação com a tabela `usuarios` no banco de dados MySQL.
* **Werkzeug Security:** Biblioteca utilizada para aplicar funções de dispersão criptográfica (hash) unidirecionais nas senhas. Nenhuma senha é armazenada em texto plano no banco de dados.

### Fluxo de Funcionamento

1. O usuário acessa a rota `/login` e submete suas credenciais através do formulário HTML.
2. O sistema verifica no banco de dados se o `username` fornecido existe.
3. Caso exista, a senha fornecida em texto plano é comparada com o hash armazenado utilizando a função `check_password_hash`.
4. Se as credenciais forem válidas, uma sessão segura é iniciada e o usuário é redirecionado para a aplicação principal (`base.html`). Se forem inválidas, mensagens de erro (Flash Messages) são exibidas na tela de login.

### Como criar o primeiro usuário (Admin)

Devido à criptografia obrigatória das senhas, não é possível inserir usuários manualmente escrevendo a senha em texto plano diretamente no painel do banco de dados.

Para criar o acesso inicial, utilize o script de configuração fornecido na raiz do projeto:

1. Certifique-se de que o ambiente virtual está ativado e as variáveis de ambiente (`.env`) estão configuradas.
2. Execute o script de criação via terminal:
```bash
   python criar_admin.py
```

---

## Sistema de Chat (Gemini)

A interface de chat comunica o front-end com a API do Gemini via HTMX, sem recarregamento de página.

### Correções Aplicadas

* **Recebimento de mensagens:** A rota `/api/enviar_mensagem` foi corrigida para ler os dados como form data (`request.form.get('user_message')`), que é o formato enviado pelo HTMX — substituindo o uso incorreto de `request.get_json()`.
* **Resposta HTML:** A rota agora retorna um fragmento HTML com os dois balões de mensagem (usuário e bot), permitindo que o HTMX os insira corretamente no histórico via `hx-swap="beforeend"`.
* **NameError em runtime:** Removida referência à variável `history` indefinida em `services.py`, que causava falha silenciosa na primeira mensagem enviada.

### Fluxo de Funcionamento

1. O usuário digita uma mensagem e o formulário é submetido via HTMX (POST em `/api/enviar_mensagem`).
2. A rota lê o campo `user_message` do form data e repassa ao `bot()`.
3. `bot()` busca contexto relevante na `BaseDeConhecimento` e monta o prompt final para o Gemini.
4. A resposta é convertida de Markdown para HTML e retornada junto com o balão do usuário.
5. O HTMX insere os dois balões no final do `#chat-messages`, sem recarregar a página.