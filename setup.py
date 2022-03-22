from setuptools import setup


setup(
    name='fast_api_app',
    version='0.0.1',
    author='Ekaterina',
    author_email='test@mail.ru',
    desription='FastApi app',
    install_requires=[
        'fastapi==0.75.0',
        'unicorn==1.0.3',
        'SQLAlchemy==1.4.32',
        'pytest==7.1.1',
        'requests==2.27.1'


    ],
    scripts=['app/main.py', 'script/create_db.py']
)