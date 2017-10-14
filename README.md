# LendApp

## ALWAYS develop locally on branches -> submit pull requests to master

Issues:

1) Having trouble with Flask-SQLAlchemy connections. I think the issue is solely related to this line in init.py:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://HARRISONS-THINK/LendApp'
