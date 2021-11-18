from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .main import user_link_validate, search_link_in_database


def home(request):
    if request.method == "POST":
        link = user_link_validate(request.POST['git_pull'])
        if link:
            link_result = search_link_in_database(link)
            if link_result:
                return render(request, 'pull_req_app/home.html', context={'user_result': link_result})
        else:
            messages.error(request,
                           f'Ссылка {request.POST["git_pull"]} некорректна. '
                           f'Пример: https://github.com/profile/some_repositories')
            return redirect('home_view')
    return render(request, 'pull_req_app/home.html')




