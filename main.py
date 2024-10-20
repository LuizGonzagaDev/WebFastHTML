
from fasthtml.common import FastHTML, serve
from componentes import gerar_titulo, gerar_formulario, lista_tarefas

app = FastHTML()

# Lista para armazenar as tarefas (de forma simples, sem banco de dados)
tarefas = []

# Rota para a homepage
@app.get("/")
def homepage():
    titulo = gerar_titulo("Minha Página de Tarefas", "Organize suas tarefas com facilidade")
    formulario = gerar_formulario()
    tarefas_html = lista_tarefas(tarefas)
    return titulo + formulario + tarefas_html

# Rota para processar o formulário e adicionar a tarefa
@app.post("/adicionar_tarefa")
def adicionar_tarefa(request):
    nova_tarefa = request.form.get("tarefa")  # Captura a nova tarefa do formulário
    if nova_tarefa:
        tarefas.append(nova_tarefa)  # Adiciona a nova tarefa à lista
    return homepage()  # Retorna à homepage para exibir a lista atualizada

# Iniciar o servidor
serve(app)
