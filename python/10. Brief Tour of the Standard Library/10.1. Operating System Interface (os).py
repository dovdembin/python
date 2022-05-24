import os
import shutil


print(os.getcwd())  # :\Users\dov_dembin\PycharmProjects\mainPython\python\10. Brief Tour of the Standard Library
os.chdir('..')  # Change current working directory
print(os.getcwd())  # C:\Users\dov_dembin\PycharmProjects\mainPython\python
print(os.system('dir'))  # Run the command in the system shell
os.chdir('10. Brief Tour of the Standard Library')
print(dir(os))  # <returns a list of all module functions>
print(help(os))  # <returns an extensive manual page created from the module's docstrings>

os.remove('./files_for_os_example_target/your.txt')
shutil.copyfile('./files_for_os_example_source/my.txt', './files_for_os_example_source/your.txt')
shutil.move('./files_for_os_example_source/your.txt', './files_for_os_example_target')


