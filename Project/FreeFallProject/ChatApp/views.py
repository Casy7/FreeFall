from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
   return HttpResponse("Hello World!")


class UserLogin(View):
    # permission_required = ('posts.can_view', 'login.can_view')
    # template_name = 'create_post.html'
    # permission_denied_message = "Sorry. Access denied"
    # raise_exception = True
    def __init__(self):
        self.error = 0
    # form_class = LoginUser

    def get(self, request):
        if self.error == 0:
            context = {'error': ''}
        else:
            context = {'error': '1'}
            self.error = 0
        # context['form'] = self.form_class()
        return render(request, "login.html", context)

    def post(self, request):
        context = {}
        form = request.POST
        validation = UserForm(request.POST)
        if validation.is_valid():
            # print(form)
            username = form['username']
            password = form['password']

            # new_post.author = Author.objects.get(id = request.POST.author)
            # new_post.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    context['name'] = username
                    return HttpResponseRedirect("/")
            else:
                self.error = 1
                # return Posts.get(self,request)
                return HttpResponse("Authentication error. Password or username is invalid.")
        else:
            return HttpResponse("Data isn't valid")

