# [Django官方文档](https://docs.djangoproject.com/en/1.11/)-Getting started

确认Django是否安装，查看Django版本
```shell
$ python -m django --version
```
## 1. Creating a project

From the command line, `cd` into a directory where you’d like to store your code, then run the following command:

```shell
$ django-admin startproject mysite
```

or:

```shell
$ django-admin startproject mysite .
```

Let’s look at what [`startproject`](https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-startproject) created:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Let’s verify your Django project works. Change into the outer `mysite` directory, if you haven’t already, and run the following commands:

```shell
$ python manage.py runserver
```

You’ll see the following output on the command line:

```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

April 23, 2017 - 15:50:53
Django version 1.11, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now that the server’s running, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your Web browser. You’ll see a “Welcome to Django” page, in pleasant, light-blue pastel. It worked!

> **Changing the port**
>
> By default, the [`runserver`](https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-runserver) command starts the development server on the internal IP at port 8000.
>
> If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:
>
> ```shell
> $ python manage.py runserver 8080
> ```
>
> If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:
>
> ```shell
> $ python manage.py runserver 0:8000
> ```

## 2. Creating the Polls app

> **Projects vs. apps**
>
> What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a simple poll app. A project is a collection of configuration and apps for a particular website. **A project can contain multiple apps. An app can be in multiple projects**.

To create your app, make sure you’re in the same directory as `manage.py` and type this command:

```shell
$ python manage.py startapp polls
```

That’ll create a directory `polls`, which is laid out like this:

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

## 3. Write your first view

