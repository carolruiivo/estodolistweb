from database import consultar_tarefas

tarefas = consultar_tarefas()
print(len(tarefas), "tarefa(s) no banco")
for t in tarefas:
    print(t)