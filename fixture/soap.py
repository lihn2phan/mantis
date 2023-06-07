from suds.client import Client
from suds import WebFault
from model.project import Project
class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['soapUrl'])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self):
        username = self.app.config['webadmin']['username']
        password = self.app.config['webadmin']['password']
        client = Client(self.app.config['web']['soapUrl'])
        projects = []
        try:
            l = client.service.mc_projects_get_user_accessible(username, password)
            for project in l:
                name = project.name
                status = project.status.name
                view_status = project.view_state.name
                description = project.description
                id = project.id
                projects.append(
                    Project(name=name, status=status, description=description, view_status=view_status, id=str(id)))
            return projects
        except WebFault:
            return []
