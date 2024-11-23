from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import now
from django.views import View


class SetTimeCookie(View):
    def get(self, request):
        return HttpResponse()

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        current_time = now()

        last_visit = request.COOKIES.get('last_visit')

        if last_visit:
            response.content = f"Your last visit was on {last_visit}".encode()
        else:
            response.content = "This is you first visit"

        response.set_cookie(
            'last_visit',
            current_time.strftime("%Y-%m-%d %H:%M:%S"),
            expires=10,
        )

        return response
