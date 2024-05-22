
from datetime import datetime
import hashlib


class Task:
    PRIORITIES = ['Do', 'Schedule', 'Delegate', 'Delete']
    STATUSES = ['Done', 'Progress', 'Cancelled']

    def __init__(self, title, description='', due_date=None, priority='Do', status='Not Started', time_to_complete=None):
        if priority not in self.PRIORITIES:
            self.raise_priority_error()
        if status not in self.STATUSES:
            self.raise_status_error()
        self.id = self.generate_id(title, description)
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.time_to_complete = time_to_complete
    
    @staticmethod
    def generate_id(title, description):
        unique_string = title + description + datetime.now().isoformat()
        return hashlib.md5(unique_string.encode()).hexdigest()


    def raise_priority_error(self):
        matrix = (
            "+------------------------+----------------------------+\n"
            "|        Do              |      Schedule              |\n"
            "|  (Urgent/Important)    | (Not Urgent/Important)     |\n"
            "+------------------------+----------------------------+\n"
            "|      Delegate          |       Delete               |\n"
            "| (Urgent/Not Important) | (Not Urgent/Not Important) |\n"
            "+------------------------+----------------------------+\n"
        )
        raise ValueError(
            f"Priority must be one of {self.PRIORITIES}\n\n"
            f"Eisenhower Matrix:\n{matrix}"
        )
    
    def raise_status_error(self):
        raise ValueError(f"Status must be one of {self.STATUSES}")

    def update(self, title=None, description=None, due_date=None, priority=None, status=None, time_to_complete=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority and priority not in self.PRIORITIES:
            self.priority = priority
        if status and status not in self.STATUSES:
            self.raise_status_error()
        if time_to_complete:
            self.time_to_complete = time_to_complete
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'time_to_complete': self.time_to_complete
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data['title'],
            description=data.get('description', ''),
            due_date=datetime.fromisoformat(data['due_date']) if data['due_date'] else None,
            priority=data.get('priority', 1),
            status=data.get('status', 'Progress'),
            time_to_complete=data.get('time_to_complete')
        )
        task.id = data['id']
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.updated_at = datetime.fromisoformat(data['updated_at'])
        return task

