import jinja2
import os


def start(proj_dir, **kwargs):
    if os.path.exists(proj_dir):
        print(f'{proj_dir} already exists！')
        exit(2)

    template_dir = os.path.join(os.path.dirname(__file__), 'template', 'default')
    template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
    template_env = jinja2.Environment(loader=template_loader)

    if os.path.isdir(template_dir):
        for root, dirs, files in os.walk(template_dir):
            new_project_dir = root.replace(template_dir, proj_dir)
            current_dir = root.replace(template_dir, '')
            os.makedirs(f'{new_project_dir}')
            for file in files:
                # 如果不是jinja2的文件则跳过
                # if not file.endswith(".jinja2"):
                #     continue

                template = template_env.get_template(os.path.join(current_dir, file))
                result = template.render()
                with open(os.path.join(new_project_dir, file.rstrip('.jinja2')), "w") as f:
                    f.write(result)
