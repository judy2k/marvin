import json

from django.conf import settings
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView, View

import slackclient


slack = slackclient.SlackClient(
    token=settings.BOT_API_TOKEN,
)


class AccountProfileView(TemplateView):
    template_name = "website/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slack.api_call(
            "chat.postMessage",
            channel="@judy2k",
            as_user=True,
            text="Hello from Python! :tada:"
        )

        return context


@method_decorator(csrf_exempt, name='dispatch')
class SlackEventHandler(View):
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)

        from pprint import pprint
        pprint(payload)

        if payload['type'] == 'url_verification':
            return HttpResponse(
                payload['challenge'],
                content_type='application/x-www-form-urlencoded',
            )
        elif payload['type'] == 'event_callback':
            event = payload['event']
            if event['type'] == 'team_join':
                user_id = event['user']['id']
                slack.api_call(
                    "chat.postMessage",
                    channel=user_id,
                    as_user=True,
                    text="Hello from Python! :tada:"
                )

        return HttpResponse("OK")
