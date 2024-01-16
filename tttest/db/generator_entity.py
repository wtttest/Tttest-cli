# -*- coding: utf-8 -*-
# @Time : 2024/1/9 15:08
from jinja2 import Environment, FileSystemLoader
import os
from tttest.db.get_table_structure import get_table_structure


def generate(table,project_path,target_path = os.getcwd()):
    # if  project_path
    project_Name = os.path.basename(project_path)

    template_Loader = FileSystemLoader(searchpath=(os.path.dirname(__file__)).replace('\\','/'))
    template_Env = Environment(loader=template_Loader)
    tpl = template_Env.get_template('template.py.jinja2')

    structures = get_table_structure(table,project_Name)
    for structure in structures:
        # 在tttest生成的结构目录下生成数据表实体 current_Dir生成的目录，生成的文件，class_Name类名
        current_Dir = os.path.join(project_path ,'domain')
        new_Dir = os.path.join(current_Dir, structure[0]) + '_mapper.py'
        class_Name = os.path.basename(os.path.join(current_Dir, structure[0].title().replace("_", "")) + 'Mapper')
        table_Name = structure[0]
        print(new_Dir)
        with open(new_Dir, 'w',encoding='utf-8') as f:

            result = tpl.render(table=structure[1],class_Name=class_Name,table_Name=table_Name)
            f.write(result)


