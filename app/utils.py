from dataclasses import dataclass

@dataclass
class Project:
    name: str
    desc: str
    link: str

class User:
    def __init__(self) -> None:  
        self.hobbies = ["Football", "Video Games", "Watching Aurora"]
        self.work_experience = ["SWE @ Incorta     2021-2024", "SWE Intern @ M3ntorship      01/2021-04/2021"]
        self.education = ["M.Sc. @ TTU     2024-2026", "B.Sc. @ Alexandria University    2026-2021"] 
        self.projects: Project = [Project(name='Foo', desc='Foo Desc', link='https://github.com/')]