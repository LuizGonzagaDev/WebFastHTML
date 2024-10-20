
from fasthtml.common import FastHTML, serve
from componentes import gerar_titulo, gerar_formulario, lista_tarefas

# Inicializando o aplicativo
app = FastHTML()

# Lista simples para armazenar as tarefas (pode ser substituído por um banco de dados)
tarefas = []

# Definindo a rota principal (homepage)
@app.get("/")
def homepage():
    titulo = gerar_titulo("Página de Tarefas", "Adicione e organize suas tarefas")
    formulario = gerar_formulario()
    tarefas_html = lista_tarefas(tarefas)
    return titulo + formulario + tarefas_html

# Definindo a rota para processar o formulário e adicionar a tarefa
@app.post("/adicionar_tarefa")
def adicionar_tarefa(request):
    nova_tarefa = request.form.get("tarefa")  # Captura a nova tarefa do formulário
    if nova_tarefa:
        tarefas.append(nova_tarefa)  # Adiciona a tarefa à lista
    return homepage()  # Retorna à homepage com a lista atualizada

# Iniciando o servidor
if __name__ == "__main__":
    serve(app)
