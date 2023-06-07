from model.project import Project
from random import randint
import random
def test_del_project(app):

    old_list_projects = app.soap.get_project_list()
    if len(old_list_projects) == 0:
        project = Project(name=f"name_project{randint(0, 5000)}", description="description_project")
        app.project.create(project)
        old_list_projects = app.project.get_projects_list()
    project = random.choice(old_list_projects)
    app.project.delete(project)

    new_list_projects = app.soap.get_project_list()
    old_list_projects.remove(project)

    assert len(old_list_projects) == len(new_list_projects)
    assert sorted(new_list_projects, key=Project.id_or_max) == sorted(old_list_projects, key=Project.id_or_max)
