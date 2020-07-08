from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

#model task table class
class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task_description


class ToDoList:

    def __init__(self, db_name='todo.db'):
        engine = create_engine(f'sqlite:///{db_name}?check_same_thread=False')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add(self, task_desk):
        new_row = Table(task=task_desk)
        self.session.add(new_row)
        self.session.commit()

    def show_today(self):
        rows = self.session.query(Table).all()
        print('Today:')
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for number, item in enumerate(rows, 1):
                print(f'{number}) {item.task}')


tasks = ToDoList()
while True:
    print('1) Today\'s tasks')
    print('2) Add task')
    print('0) Exit')
    user_command = input()
    if '2' == user_command:
        task = input('Enter task\n')
        tasks.add(task)
    elif '1' == user_command:
        tasks.show_today()
    elif '0' == user_command:
        print('Bye!')
        break
