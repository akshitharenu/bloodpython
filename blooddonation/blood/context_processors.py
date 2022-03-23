from .models import UserRegistration
def menu_links(request):
    links=UserRegistration.objects.all()
    return dict(links=links)