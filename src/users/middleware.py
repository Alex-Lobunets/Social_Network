from django.contrib.auth import get_user_model
from django.utils import timezone

CustomUser = get_user_model()


def update_activity(get_response):
    def middleware(request):
        response = get_response(request)
        if request.user.id:
            if CustomUser.objects.filter(id=request.user.id).exists():
                user = CustomUser.objects.get(id=request.user.id)
                user.last_activity = timezone.now()
                user.save()
        return response
    return middleware
