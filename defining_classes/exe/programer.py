class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        needed_skills = self.skills - skills_needed
        if needed_skills < 0:
            return f"{self.name} needs {abs(needed_skills)} more skills"
        if not new_language == self.language:
            previous_language = self.language
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}"
        else:
            return f"{self.name} already knows {new_language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))