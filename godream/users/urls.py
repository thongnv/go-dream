from django.conf.urls import url

from .views import login

namespace_prefix = "godream.users."

urlpatterns = [
    # url(r'^register/$', UserRegister.as_view(),
    #     name=namespace_prefix + "user_register"),
    url(r'^login/$', login,
        name=namespace_prefix + "login"),
    # url(r'^logout/$', Logout.as_view(),
    #     name=namespace_prefix + "logout")
]
