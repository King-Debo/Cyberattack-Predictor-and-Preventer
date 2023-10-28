# Step 7: Use django.contrib.auth and django-crispy-forms libraries to add authentication and form validation features to the website.

# Import the necessary modules
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Define a custom user creation form that inherits from UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Add a helper attribute to customize the form layout using crispy forms
    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("username", css_class="form-group col-md-6 mb-0"),
            Column("email", css_class="form-group col-md-6 mb-0"),
            css_class="form-row",
        ),
        Row(
            Column("password1", css_class="form-group col-md-6 mb-0"),
            Column("password2", css_class="form-group col-md-6 mb-0"),
            css_class="form-row",
        ),
        Submit("submit", "Sign up"),
    )

    # Define the meta class to specify the model and the fields of the form
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# Define a custom authentication form that inherits from AuthenticationForm
class CustomAuthenticationForm(AuthenticationForm):
    # Add a helper attribute to customize the form layout using crispy forms
    helper = FormHelper()
    helper.form_method = "POST"
    helper.layout = Layout(
        Row(
            Column("username", css_class="form-group col-md-6 mb-0"),
            Column("password", css_class="form-group col-md-6 mb-0"),
            css_class="form-row",
        ),
        Submit("submit", "Log in"),
    )

# Define a view for creating a new user account using the custom user creation form
class SignUpView(CreateView):
    # Specify the template name, the form class, and the success URL
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")

# Define a view for logging in an existing user using the custom authentication form
class LogInView(FormView):
    # Specify the template name, the form class, and the success URL
    template_name = "registration/login.html"
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("home")

    # Override the form_valid method to log in the user after validating the form
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

# Define a view for logging out an existing user
def log_out_view(request):
    # Log out the user and redirect to the home page
    logout(request)
    return redirect("home")

# Define a view for displaying the prediction input form to the user
@login_required # Require the user to be logged in to access this view
def predict_view(request):
    # Render a template with the prediction input form
    return render(request, "predictor/predict.html")

# Define a view for displaying the prevention tips to the user
@login_required # Require the user to be logged in to access this view
def prevention_view(request):
    # Get the prevention tips from the database as a list of strings
    tips = PreventionTip.objects.values_list("tip", flat=True)

    # Convert the list of strings to a JSON object
    tips = json.dumps(list(tips))

    # Render a template with the prevention tips as context data
    return render(request, "predictor/prevention.html", {"tips": tips})

# Add the URL patterns for the new views in urls.py
from django.contrib import admin
from django.urls import path, include
from predictor.views import SignUpView, LogInView, log_out_view, predict_view, prevention_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("predictor.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LogInView.as_view(), name="login"),
    path("logout/", log_out_view, name="logout"),
    path("predict/", predict_view, name="predict"),
    path("prevention/", prevention_view, name="prevention"),
]
