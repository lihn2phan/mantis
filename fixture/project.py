from model.project import Project
class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # нажать create new projects
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # заполнить поля и подтвердить
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_css_selector("input.button").click()

    def delete(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_css_selector("input.button").click()

    def open_projects_page(self):
        wd = self.app.wd
        # открыть базовую страницу
        self.app.open_home_page()
        # открыть страницу manage
        wd.find_element_by_link_text("Manage").click()
        # открыть manage projects
        wd.find_element_by_link_text("Manage Projects").click()

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        l = list(wd.find_elements_by_css_selector("tr[class*=row]")) # все строки которые есть на странице
        element = wd.find_elements_by_css_selector("tr[class*=row-category]") # все строки-заголовки которые есть на странице
        index = l.index(element[1]) # индекс второй строки-заголовка
        count_row = len(l[1:index])
        return count_row
    def get_projects_list(self):
        wd = self.app.wd
        self.open_projects_page()
        count = self.count()
        lines = wd.find_elements_by_css_selector("tr[class*=row]")
        projects = []
        for i in range(1, count+1):
            element = lines[i]
            cells = element.find_elements_by_css_selector("td")
            name = element.find_element_by_css_selector("a").text
            status = cells[1].text
            view_status = cells[3].text
            description = cells[4].text
            id = element.find_element_by_css_selector("a").get_attribute("href").split("id=")[-1]
            projects.append(Project(name=name, status=status, description=description, view_status=view_status, id=str(id)))
        return projects

    def project_in_list(self, project, projects):
        for p in projects:
            if p.name == project.name and p.description == project.description:
                return p.id
        return "-1"

    # ввод пароля на всякий, в итоге не нужен вроде, но пусть будет
    def fill_password(self, password):
        wd = self.app.wd
        try:
            wd.find_element_by_name("password").click()
            wd.find_element_by_name("password").clear()
            wd.find_element_by_name("password").send_keys(password)
            wd.find_element_by_css_selector('input[type="submit"]').click()
        except:
            return
