class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task Name: {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        task_exists = [t for t in self.tasks if t.name == task_name]
        if not task_exists:
            return f"Could not find task with the name {task_name}"
        task_exists[0].completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        counter = 0
        for el in self.tasks:
            if el.completed:
                counter += 1
                self.tasks.remove(el)
            else:
                pass
        return f"Cleared {counter} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for el in self.tasks:
            res += f"Name: {el.details()}\n"
        return res

