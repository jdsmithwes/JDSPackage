"""Main module."""

#Functions for header info in notebooks to automate including your name, date, and version number of a notebook

#Header puts your name and current date

def Header(name, project_name, date):
    name = {'first': 'Jamaal', 'last': 'Smith'}
    project_name = 'Flatiron School Capstone Project'
    date = datetime.today()
    print(name['first'], name['last'])
    print (project_name)
    print (date)