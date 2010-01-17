import sys
try:
    from d51.django.virtualenv.test_runner import run_tests
except ImportError:
    print "Please install d51.django.virtualenv.test_runner to run these tests"

def setUp():
    from django.conf.urls.defaults import patterns, include, handler500, handler404
    sys.modules[setUp.__module__].handler500 = handler500
    sys.modules[setUp.__module__].handler404 = handler404
    sys.modules[setUp.__module__].urlpatterns = patterns('',
        (r'^blog/', include('d51.django.apps.blogs.urls')),
    )


def main():
    settings = {
        "INSTALLED_APPS": (
            "django.contrib.contenttypes",
            "d51.django.apps.blogs",
        ),
        'ROOT_URLCONF': '__main__',
    }
    run_tests(settings, 'blogs')

if __name__ == '__main__':
    main()
