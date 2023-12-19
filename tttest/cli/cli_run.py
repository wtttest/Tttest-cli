import argparse

from tttest.cli.generator import render
from tttest.config.cfg import l
from tttest.version import __version__


def run():
    # print('run command')
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=f'TtTest v{__version__}',
                        help=("显示版本号", 'display tttest version')[l.n])
    parser.add_argument('--lang', choices=['zh', 'en'],
                        help=("设置工具语言", 'set language')[l.n])
    parser.add_argument('--new', metavar='project_dir',
                        help=("创建新项目目录", "create a project folder")[l.n])

    args = parser.parse_args()

    # 看命令行中是否设置了语言
    if args.lang:
        l.n = l.LANGS[args.lang]

    if args.new:
        # print('new command >> tttest is running...', args)
        render.start(args.new)
