from fabric.api import env, cd, sudo, settings
from fabric.colors import green
from os.path import join


proj_repo = 'https://github.hogarthww.prv/lukeperrottet/pingpongproject.git'
proj_root = '/opt/hogarth'
req = 'git python python-dev python-pip nginx supervisor'


def vagrant_settings():
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']


def prod_settings():
    env.user = 'devadm'
    env.hosts = ['10.9.4.107:22']


def clone():
    sudo('mkdir -p %s' % proj_root)
    with cd(proj_root):
        sudo('export GIT_SSL_NO_VERIFY=1 && git clone %s' % proj_repo)


def setup():
    sudo('apt-get install -y {0}'.format(req))

    with settings(warn_only=True):
        clone()

    with cd(join(proj_root, 'pingpongproject')), settings(warn_only=True):
        sudo('pip install -r requirements.txt')

    with cd(join(proj_root, 'pingpongproject/pingpongproject/')), settings(
            warn_only=True):
        sudo('python manage.py migrate')
        sudo('python manage.py add_superuser')

    with settings(warn_only=True):
        sudo('useradd -m -s /bin/bash -p projadm projadm')

    path = join(proj_root, 'pingpongproject/nginx_supervisor_setup/')
    with cd('/etc/nginx/sites-available/'), settings(warn_only=True):
        '''
        This is line below copy the content of the nginx text file
        to the supervisor config file but without the DOS carriage
        returns (translating by ^M in Unix)
        and replace it by Unix carriage returns
        '''
        sudo("tr '\015' '\n' < {0} > pingpong".format(
            join(path, 'nginx.txt')
            )
        )
        sudo('ln -s /etc/nginx/sites-available/pingpong \
            /etc/nginx/sites-enabled/pingpong')

    with cd('/etc/nginx/sites-available/'), settings(warn_only=True):
        sudo('rm -r default')

    with cd('/etc/supervisor/conf.d/'), settings(warn_only=True):
        sudo("tr '\015' '\n' < {0} > pingpong.conf".format(
            join(path, 'supervisor.txt')
            )
        )

    path = join(proj_root, 'pingpongproject/pingpongproject')
    with cd(path):
        sudo('python manage.py collectstatic')

    sudo('supervisorctl reread')
    sudo('supervisorctl reload')
    sudo('service nginx restart')

    print green('Set-up successfully done !')


def runserver():
    sudo('supervisorctl restart pingpong')


def deploy():
    path = join(proj_root, 'pingpongproject')
    with cd(path):
        sudo('export GIT_SSL_NO_VERIFY=1 && git pull')
    path = join(proj_root, 'pingpongproject/pingpongproject')
    with cd(path):
        sudo('python manage.py migrate')
        sudo('python manage.py collectstatic')
    runserver()
