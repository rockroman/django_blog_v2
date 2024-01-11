from allauth.account.views import LogoutView
from django.shortcuts import redirect


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Clear your custom session data
        print(
            "Before logout, viewed_object_slug in session:",
            request.session.get("viewed_object_slug"),
        )
        request.session.pop("viewed_object_slug", None)
        print(
            "After logout, viewed_object_slug in session:",
            request.session.get("viewed_object_slug"),
        )

        # Call the parent class's dispatch method
        return super().dispatch(request, *args, **kwargs)
