from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.humanize.templatetags.humanize import naturaltime
from ..data_structure.models import Message
from django.http.response import JsonResponse


class TalkMain(LoginRequiredMixin, View):
    def get(self, req):
        return render(req, 'chat/talk.html')

    def post(self, req):
        message = Message(text=req.POST['message'], owner=req.user)
        message.save()
        return redirect(reverse('chat:talk'))


class TalkMessages(LoginRequiredMixin, View):
    def get(self, req):
        messages = Message.objects.all().order_by('-create_at')[:10]
        res = []
        for msg in messages:
            re = [msg.text, naturaltime(msg.create_at)]
            res.append(re)
        return JsonResponse(res, safe=False)

