import os


def get_cwd() -> str:
    directory = os.path.basename(os.getcwd())
    print('Current directory =', directory)
    return directory


if __name__ == '__main__':
    get_cwd()
