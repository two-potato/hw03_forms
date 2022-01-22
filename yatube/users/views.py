from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .forms import CreationForm
# from .forms import CreationForm, ChangePassForm, ResetPassForm
# from django.contrib.auth.views import PasswordChangeView



class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


# class PasswordChangeView(PasswordChangeView):
#     form_class = ChangePassForm
#     # auth/password_change/
#     success_url = reverse_lazy('users:password_change_done')
#     template_name = 'users/password_change_form.html'
#     # def get_form_kwargs(self):
#     #         kwargs = super(PasswordChangeView, self).get_form_kwargs()
#     #         kwargs['user'] = self.request.user
#     #         if self.request.method == 'POST':
#     #             kwargs['data'] = self.request.POST
#     #         return kwargs


# class PasswordChangeDoneView(TemplateView):
#     # auth/password_change/done/
#     # success_url=reverse_lazy('users:password_change_done')
#     template_name = 'users/password_change_done.html'


# class PasswordResetView(UpdateView):
#     # auth/password_reset/
#     form_class = ResetPassForm
#     success_url = reverse_lazy('users:password_reset_done')
#     template_name = 'users/password_reset_form.html'


# class PasswordResetDoneView(TemplateView):
#     # auth/password_reset/done/
#     success_url = reverse_lazy('users:password_reset_done')
#     template_name = 'users/password_reset_done.html'


# class PasswordResetConfirmView(TemplateView):
#     # auth/reset/<uidb64>/<tocken>/
#     success_url = reverse_lazy('users:cange_pass_done')  # ??????? check url
#     template_name = 'users/password_reset_confirm.html'


# class PasswordResetCompleteView(TemplateView):
#     # auth/reset/done/
#     success_url = reverse_lazy('users:password_reset_complete')
#     template_name = 'users/password_reset_complete.html'
