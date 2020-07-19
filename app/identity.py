
from django.http import HttpResponse, HttpResponseRedirect


def islogin(func):
    '''身份认证装饰器，
    :param func:
    :return:
    '''
    def wrapper(request, *args, **kwargs):
        if not request.session.get("is_login",False):
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return func(request, *args, **kwargs)

    return wrapper