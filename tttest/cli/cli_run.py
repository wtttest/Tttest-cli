import argparse
from tttest.version import __version__
from tttest.cli.generator import render
from tttest.config.cfg import l


def run():
    print('run command >> tttest is running...')
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'TtTest v{ __version__}',
                        help=("显示版本号", 'display tttest version')[l.n])
    
    parser.add_argument('--new',metavar='project_dir',help=("创建项目目录",'create project directory')[l.n])
    
    parser.add_argument('--lang', choices=['zh', 'en'],
                        help=("设置工具语言", 'set language')[l.n])
    
    args = parser.parse_args()
    if args.new:

        render.create(args.new)



    
    


    
