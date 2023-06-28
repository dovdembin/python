# https://www.youtube.com/watch?v=2Fp1N6dof0Y

import subprocess


def subprocess_methods():
    p1 = subprocess.run(['dir', '/N'], shell=True, text=True)  # same subprocess.run('dir', shell=True)
    print(p1.args)  # ['dir', '/N']
    print(p1.returncode)  # 0
    print(p1.stdout)


def pipe_and_text():
    # "capture_output=True" is the same as "stdout=subprocess.PIPE" but it is sending to the PIPE
    p1 = subprocess.run(['dir', '/N'], shell=True, stdout=subprocess.PIPE,
                        text=True)  # same subprocess.run('dir', shell=True)

    print(p1.stdout)


def decode_():
    p1 = subprocess.run(['dir', '/N'], shell=True, capture_output=True)  # same subprocess.run('dir', shell=True)
    print(p1.stdout.decode())


def subprocess_return_code():
    # file does not exist
    p1 = subprocess.run(['dir', '/N', 'dne'], shell=True, capture_output=True, text=True)

    if p1.returncode == 0:
        print("success")
    else:
        print(p1.returncode)  # 1
        print(p1.stderr)  # File Not Found


def redirect_to_file():
    with open('output.txt', 'w') as f:
        p1 = subprocess.run(['dir', '/N'], shell=True, stdout=f, text=True)


# def check_stderr():
#     p1 = subprocess.run(['dir', '/N', 'dne'], shell=True, capture_output=True, text=True, check=True)  # returned non-zero exit status 1


def redirect_devnull():
    p1 = subprocess.run(['dir', '/N', 'dne'], shell=True, stderr=subprocess.DEVNULL, text=True)
    print(p1.stderr)


def standard_out():
    p1 = subprocess.run('type output.txt | findstr file', shell=True, capture_output=True, text=True)
    print(p1.stdout)
    # same as
    p1 = subprocess.run(['type', 'output.txt'], shell=True, capture_output=True, text=True)
    p2 = subprocess.run(['findstr', 'file'], shell=True, capture_output=True, text=True, input=p1.stdout)
    print(p2.stdout)


# subprocess_methods()
# redirect_to_file()
# pipe_and_text()
# decode_()
# subprocess_return_code()
# # check_stderr()
# redirect_devnull()
standard_out()
