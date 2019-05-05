from django.apps import AppConfig
# from urllib import request


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from updater import update
        update.start()
