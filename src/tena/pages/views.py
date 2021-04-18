from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.utils.decorators import classonlymethod
from django.views.generic import RedirectView, TemplateView, View


class HomePage(TemplateView):
    template_name = "pages/index.html"


class MessageView(RedirectView):
    url = "/"
    message = None
    level = None

    @classonlymethod
    def as_view(cls, **initkwargs):
        message = initkwargs.get("message", None)
        level = initkwargs.get("level", "SUCCESS")
        if message is None:
            raise ImproperlyConfigured("Message is not included in kwargs.")
        if level.upper() not in messages.DEFAULT_LEVELS.keys():
            raise ImproperlyConfigured(
                "Unknown level. Level should be one of the following %s.",
                ", ".join(messages.DEFAULT_LEVELS.keys()),
            )
        initkwargs.update({"level": messages.DEFAULT_LEVELS.get(level)})
        return super().as_view(**initkwargs)

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, self.level, self.message)
        return super().dispatch(request, *args, **kwargs)


class SendMessageView(View):
    def get(self, request, *args, **kwargs):
        msg = kwargs.get("msg", None)
        messages.add_message(request, 20, msg)
        return HttpResponseRedirect("/")
