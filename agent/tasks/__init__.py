def get_all_jobs():
    """
    TODO: This function should return all the available functions that the agent can perform.
    Our Agent will dynamically load all the available jobs from this function.
    
    So how?

    Each handler class has its member functions. Those functions must have docstrings that describe the job.
    Agent will read those docstrings and do similarity search to find the most relevant job for the user query.

    Each member functions **MUST NOT** have its own returns.
    Instead, it should return the result to QueryWrapper object.

    TODO: We need to refactor the handler classes to follow this rule.
    """
    pass
    # for name, member in RiotHandler.__class__.__dict__.items():
    #     if callable(member):
    #         print(f"{name}: {member.__doc__}")