from django.conf.urls.defaults import patterns

urlpatterns = patterns('db.views',
    (r'^$', 'index'),
)
