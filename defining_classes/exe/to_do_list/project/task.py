from datetime import datetime

from project.section import Section


class Task:

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if not new_name == self.name:
            self.name = new_name
            return new_name
        return f"Name cannot be the same."

    def change_due_date(self, new_date: str):
        for fmt in ("%d.%m.%Y", "%d/%m/%Y"):
            try:
                current_date = datetime.strptime(self.due_date, fmt)
            except ValueError:
                pass
        next_date = datetime.strptime(new_date, "%d.%m.%Y")
        if not current_date == next_date:
            self.due_date = new_date
            return new_date
        return f"Date cannot be the same."

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number not in range(len(self.comments)):
            return f"Cannot find comment."
        # if not self.comments[comment_number]:
        #     return f"Cannot find comment."
        self.comments[comment_number] = new_comment
        if 2 > len(self.comments) > 0:
            res = f"{self.comments[0]}"
            return res
        else:
            res = f"{self.comments[0]}"
            for el in range(1, len(self.comments)):
                res += f", {self.comments[el]}"
            return res

    def details(self):
        return f"{self.name} - Due Date: {self.due_date}"


# d = datetime.strptime("27/05/2020", "%d/%m/%Y")
# n = datetime.strptime("27.05.2020", "%d.%m.%Y")
# print(d == n)

# task = Task("Make bed", "27/05/2020")
# print(task.change_name("Go to University"))
# print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# # task.add_comment("Don't forget money")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# # print(section.complete_task("Make bed"))
# print(section.clean_section())
# print(section.view_section())


# section = Section("New section")
# task = Task("Tst", "27.04.2020")
# print(section.add_task(task))

# task = Task("Tst", "27.04.2020")
# print(task.change_due_date("21.05.2020"))
# print(task.due_date)