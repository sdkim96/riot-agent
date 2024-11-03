class BaseRiotAgentException(Exception):
    """Basic Exception."""
    pass


class TaskCantBeAdded(BaseRiotAgentException):
    """This Exception occurs when Jobs can't be dynamically added."""
    def __init__(self, task_id=None, message="Task can't be added to the queue"):
        self.task_id = task_id
        super().__init__(f"{message}: {task_id}" if task_id else message)