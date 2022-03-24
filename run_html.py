from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates_2')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(title='Домашнее задание')

print(msg)
