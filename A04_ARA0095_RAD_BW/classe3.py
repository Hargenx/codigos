from dataclasses import dataclass
@dataclass
class Task:
    titulo: str
    descricao: str
    concluida: bool = False
class TaskManager:
    def __init__(self: object) -> None:
        '''
        Construtor da classe TaskManager
        :return: None
        '''
        self.tasks = []
    def adicionar_tarefa(self: object, task: Task) -> None:
        '''
        Método para adicionar uma tarefa à lista de tarefas
        :param task: Task -> Tarefa a ser adicionada
        :return: None
        '''
        self.tasks.append(task)
    def listar_tarefas(self: object) -> None:
        '''
        Método para listar todas as tarefas
        :return: None
        '''
        for task in self.tasks:
            status = "Concluída" if task.concluida else "Pendente"
            print(f"Título: {task.titulo}, Descrição: {task.descricao}, Status: {status}")
    def marcar_concluida(self: object, titulo: str) -> None:
        '''
        Método para marcar uma tarefa como concluída
        :param titulo: str -> Título da tarefa a ser marcada como concluída
        :return: None
        '''
        for task in self.tasks:
            if task.titulo == titulo:
                task.concluida = True
                print(f"Tarefa '{task.titulo}' marcada como concluída.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.adicionar_tarefa(Task("Fazer compras", "Comprar leite e pão"))
    task_manager.adicionar_tarefa(Task("Estudar Python", "Resolver exercícios"))
    task_manager.listar_tarefas()
    task_manager.marcar_concluida("Fazer compras")
    task_manager.listar_tarefas()