import argparse

__requirements__ = 'requirements.txt'

import pkg_resources
from path import Path


def check_requirements():
    requirements = [f'{x.name}{x.specifier}' for x in pkg_resources.parse_requirements(Path(__requirements__).open())]
    check_requirement(requirements)


def check_requirement(requirement):
    try:
        pkg_resources.require(requirement)
    except pkg_resources.DistributionNotFound as err:
        print(f'缺少依赖包，请检查{err.req}包是否正确安装')
        exit(0)
    print(f'{"".join(requirement)} 已安装')


def generate(args):
    if args.requirements:
        check_requirements()
    else:
        check_requirement('Django')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start a django project.')
    parser.add_argument('-n', '--name', type=str, required=True, help='Name of the project.')
    parser.add_argument('-r', '--requirements', action='store_true', help='Check requirements or not.')
    parser.add_argument('-c', '--config', type=str, help='Path to the configuration file.')
    parser.add_argument('-u', '--user', action='store_true', help='Need user model or not.')
    generate(parser.parse_args())
