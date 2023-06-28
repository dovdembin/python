"""
https://www.youtube.com/watch?v=APOPm01BVrk



# inside folder C:\Users\dov_dembin\PycharmProjects\venv do:
1. python -m venv project_env
# to activate
2. project_env\Scripts\activate.bat
# where python shows where python is installed
3. where python
shows what is install in the environment
4. pip list
diactivate
5.(project_env) C:\Users\dov_dembin\PycharmProjects\venv>deactivate

============== install new project with previous requirements ==================

1. python -m venv my_project\venv
2. my_project\venv\Scripts\activate.bat
3. pip install -r requirements.txt # will use the previous requirements.txt file previously created.

================ project with global environemnt like my machine ======================

1. python -m venv venv --system-site-packages
2. venv\Scripts\activate.bat
# now every package will be install only on this environment
# to list only local packages do
3. pip list --local
# create a requirements.txt with only local install packages
4. pip freeze --local
"""