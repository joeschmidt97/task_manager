from task import Task
import json


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, **kwargs):
        task = self.get_task_by_id(task_id)
        if task:
            task.update(**kwargs)

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self):
        return [task.to_dict() for task in self.tasks]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            self.tasks = [Task.from_dict(data) for data in tasks_data]


# Example usage
if __name__ == '__main__':
    task_manager = TaskManager()
    
    # Create a new task
    task1 = Task(title='Write report', description='Write the quarterly report', due_date=datetime(2024, 5, 30), priority=1)
    task_manager.add_task(task1)

    # Update a task
    task_manager.update_task(0, status='In Progress')

    # List tasks
    for task in task_manager.list_tasks():
        print(task)

    # Save tasks to file
    task_manager.save_to_file('tasks.json')

    # Load tasks from file
    task_manager.load_from_file('tasks.json')
    for task in task_manager.list_tasks():
        print(task)

