"""Get django version
 import django
 django.get_version()
"""

"""Create django prjecrt
 django-admin startproject mysite
"""

"""
cd mysite
python manage.py migrate
python manage.py sqlmigrate blog 0001
python manage.py makemigrations blog
python .\manage.py startapp blog

python manage.py createsuperuser

python manage.py shell
    from django.contrib.auth.models import User
    from blog.models import Post
    user = User.objects.get(username='admin')
    post = Post(title='Another post',
                slug='another-post',
                body='Post body.',
                author=user)
    post.save()
"""

