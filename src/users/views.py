from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView, UserDetailsView


class MyRegisterView(RegisterView):
    """
    Return JWT Token and User.
    """


class MyLoginView(LoginView):
    """
    Return JWT Token and User.
    """


class MyUserDetailsView(UserDetailsView):
    """
    Return User.
    """


MyLoginView = MyLoginView.as_view()
MyUserDetailsView = MyUserDetailsView.as_view()
MyRegisterView = MyRegisterView.as_view()
