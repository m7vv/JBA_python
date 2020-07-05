# Write your code here
class ToDoList:

    def __init__(self):
        self.task_list = {}

    def add(self, task_name, day='today'):
        if day in self.task_list:
            self.task_list[day].append(task_name)
        else:
            self.task_list[day] = [task_name]

    def show_today(self):
        if 'today' in self.task_list:
            print('Today:')
            for number, task in enumerate(self.task_list['today'], 1):
                print(f'{number}) {task}')
        else:
            print('Today you don\'t have tasks')


tasks = ToDoList()
tasks.add('Do yoga')
tasks.add('Make breakfast')
tasks.add('Learn basics of SQL')
tasks.add('Learn what is ORM')
tasks.show_today()
