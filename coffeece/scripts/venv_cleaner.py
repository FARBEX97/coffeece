import argparse
import os
import shutil


def parser():
    """Takes arguments in case used as script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-vn", "--venvname", help="Delete all folders with the given name inside the current directory. Default venv name is 'venv'")
    args = parser.parse_args()
    if args.venvname:
        venvname = args.venvname
    else:
        venvname = 'venv'
    return args, venvname


def delete_all_venvs(args, venvname):
    # list all venvs
    cwd = os.getcwd()
    os.chdir(cwd)
    venvs = []

    for (root, dirs, files) in os.walk(cwd, topdown=True):
        for directory in dirs:
            if directory == venvname:
                venvs.append(root + os.sep + venvname)
    os.chdir(cwd)

    # delete all venvs
    for venv in venvs:
        shutil.rmtree(venv)


def main():
    args, venvname = parser()
    delete_all_venvs(args, venvname)


if __name__ == "__main__":
    main()    