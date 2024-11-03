import inspect
from .tasks import TaskPool

def get_all_available_tasks():
    """
    TODO: This function should return all the available functions that the agent can perform.
    Our Agent will dynamically load all the available jobs from this function.
    
    So how?

    Each task functions must have docstrings that describe the job. (tasks.py)
    Agent will read those docstrings and do similarity search to find the most relevant job for the user query.

    Each functions **MUST NOT** have its own returns.
    Instead, it should return the result to QueryWrapper object.
    """
    task_pool = {}

    for name, member in inspect.getmembers(TaskPool, predicate=inspect.isfunction):
        task_data = {
            name: {
                "description": member.__doc__,
                "function": member
            }
        }
        
        task_pool.update(task_data)

    return task_pool