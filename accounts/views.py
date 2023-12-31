from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import *
from django.contrib.auth.forms import *
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from accounts.forms import ProfileEdit, SignUpForm, CustomLoginForm


# Create your views here.


def signup_success(request):
    # 会員登録成功画面
    '''アカウント
    '''
    template_name = 'accounts/signup_success.html'
    return render(request, template_name)


class CustomLoginView(LoginView):
    app_name = "accounts"
    authentication_form = CustomLoginForm
    form_class = CustomLoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "ログインに成功しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ログインに失敗しました")
        return super().form_invalid(form)


class SignupView(CreateView):
    app_name = "accounts"
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm):
        user = form.save()
        login(self.request, user)
        messages.add_message(self.request, messages.SUCCESS, "ユーザー登録しました。")
        self.object = user
        # return HttpResponseRedirect(self.get_success_url())
        return render(request=self.request, template_name='accounts/signup_success.html')

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "ユーザー登録に失敗しました。")
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    # ログアウト後のリダイレクト先を指定するためのget_success_urlメソッドをオーバーライドします。
    def get_success_url(self):
        # ログアウト後にリダイレクトしたいURLを指定します。
        return reverse_lazy('home')  # このURLをカスタマイズしてください


def profile_view(request):
    '''profileの表示をする
    '''
    if request.method == "POST":
        '''何かのボタンが押されたら
        '''
        if "edit_profile" in request.POST:
            '''編集ボタンが押されたら
            '''
            return redirect('accounts:edit_profile_view')

    return render(request, 'accounts/profile.html', {'user': request.user})


def edit_profile_view(request):
    '''profileの編集ページ
    '''
    if request.method == 'POST':
        '''何らかのボタンが押されたら
        '''
        if "save_profile" in request.POST:
            pass
            form = ProfileEdit(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile_view')  # プロフィールページにリダイレクト
        else:
            form = ProfileEdit(instance=request.user)  # ここは要検討
    else:
        form = ProfileEdit(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})
