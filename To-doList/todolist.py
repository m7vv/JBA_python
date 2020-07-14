from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# model task table class
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

    def add(self, task_desk, task_date):
        new_row = Table(task=task_desk, deadline=task_date)
        self.session.add(new_row)
        self.session.commit()
        print('The task has been added!\n')

    def show_date(self, task_date, day_name=None):
        rows = self.session.query(Table).filter(Table.deadline == task_date.date()).all()
        day_name = task_date.strftime('%A') if day_name is None else day_name
        month_name = task_date.strftime('%b')
        print(f'{day_name} {task_date.day} {month_name}:')
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for number, item in enumerate(rows, 1):
                print(f'{number}) {item.task}')
        print('')

    def show_today(self):
        self.show_date(datetime.today(), day_name='Today')

    def show_week(self):
        today = datetime.today()
        i = 0
        while i <= 6:
            week_day = today + timedelta(days=i)
            self.show_date(week_day)
            i += 1

    def show_all(self):
        print('All tasks:')
        rows = self.session.query(Table).all()
        if len(rows) == 0:
            print('Nothing is missed!')
        else:
            for number, item in enumerate(rows, 1):
                print(f"{number}) {item.task}. {item.deadline.day} {item.deadline.strftime('%b')}")
                print(item.deadline)

    def show_missed(self):
        print('Missed tasks:')
        rows = self.session.query(Table).filter(Table.deadline < datetime.today()).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('Nothing is missed!\n')
        else:
            for number, item in enumerate(rows, 1):
                print(f"{number}) {item.task}. {item.deadline.day} {item.deadline.strftime('%b')}")
                print(item.deadline)
        print('')

    def delete_missed(self):
        print('Chose the number of the task you want to delete:')
        rows = self.session.query(Table).filter(Table.deadline < datetime.today()).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('Nothing is missed!\n')
            return
        else:
            for number, item in enumerate(rows, 1):
                print(f"{number}) {item.task}. {item.deadline.day} {item.deadline.strftime('%b')}")
                print(item.deadline)
        number_of_row = int(input()) - 1
        self.session.delete(rows[number_of_row])
        self.session.commit()
        print('The task has been deleted!\n')

    def show_commands(self):
        print('1) Today\'s tasks')
        print('2) Week\'s tasks')
        print('3) All tasks')
        print('4) Missed tasks')
        print('5) Add task')
        print('6) Delete task')
        print('0) Exit')


tasks = ToDoList()
while True:
    tasks.show_commands()
    user_command = input('')
    print('')
    if '1' == user_command:
        tasks.show_today()
    elif '2' == user_command:
        tasks.show_week()
    elif '3' == user_command:
        tasks.show_all()
    elif '4' == user_command:
        tasks.show_missed()
    elif '5' == user_command:
        task_desc = input('Enter task\n')
        task_date = datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d')
        tasks.add(task_desc, task_date)
    elif '6' == user_command:
        tasks.delete_missed()
    elif '0' == user_command:
        print('Bye!')
        break
