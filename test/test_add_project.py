from model.project import Project
from random import randint
def test_add_project(app):

    old_list_projects = app.soap.get_project_list()
    #project = Project(name="name_project2282", description="description_project")
    project = Project(name=f"name_project{randint(0, 5000)}", description="description_project")
    if project in old_list_projects:
        app.project.delete(project)
        old_list_projects.remove(project)

    app.project.create(project)
    new_list_projects = app.soap.get_project_list()
    old_list_projects.append(project)

    assert len(new_list_projects) == len(old_list_projects)
    assert sorted(new_list_projects, key=Project.id_or_max) == sorted(old_list_projects, key=Project.id_or_max)


