import os
from jinja2 import Environment, FileSystemLoader, loaders


def create(project_dir):
    if os.path.exists(project_dir):
        print(f'project directory【 {project_dir} 】already exists!!!')

    else:
        cur_Dir = os.path.join(os.path.dirname(__file__), 'template', 'default')

        # jinja 路径是‘/’，不是‘\’，在不同的系统下路径不同，所以要替换
        template_Loader = FileSystemLoader(searchpath=cur_Dir.replace('\\', '/'))
        template_Env = Environment(loader=template_Loader)
        for dirpath, dirnames, filenames in os.walk(cur_Dir):
            new_project_dir = dirpath.replace(cur_Dir,project_dir)
            new_dir = dirpath.replace(cur_Dir,'')
            os.makedirs(new_project_dir, exist_ok=True)

            for filename in filenames:
                template = template_Env.get_template(os.path.join(new_dir,filename).replace('\\', '/'))
                result = template.render()
                with open(os.path.join(new_project_dir,filename.rstrip('.jinja2')), 'w') as f:
                    f.write(result)
        print(f'project directory【 {project_dir} 】create successfully!')



