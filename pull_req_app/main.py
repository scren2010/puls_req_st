import requests
from bs4 import BeautifulSoup
from .models import UserRequestResult, UserRequest


def get_soup(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def user_link_validate(link):
    if link.startswith('https://github.com'):
        if not link.endswith('/pulls'):
            link += '/pulls'
            if requests.get(link).status_code != 200:
                return
            return link
        return link
    return


def search_link_in_database(link):
    user_request = UserRequest.objects.filter(user_link=link).first()
    if user_request:
        user_result = UserRequestResult.objects.filter(user_link=user_request)
        return user_result
    else:
        UserRequest.objects.create(user_link=link)
        return get_pulls(link)


def get_pulls(user_link):
    soup = get_soup(user_link).find_all(attrs={'data-hovercard-type': 'pull_request'})
    git_link = 'https://github.com'
    git_pulls_links = list(map(lambda s: [git_link + s.get('href'), s.text], soup))
    user_req = UserRequest.objects.get(user_link=user_link)
    for link, text in git_pulls_links:
        soup = get_soup(link).find_all('form', class_='js-issue-sidebar-form')[0:2]
        pull_request_reviewers = 'No reviews'
        pull_request_assignees = 'No one assigned'
        for i in soup:
            form_div = i.find('div', 'discussion-sidebar-heading text-bold')
            form_span = i.find('span', 'css-truncate')
            if form_span.find_all('p') and ''.join(form_div.text.split()) == 'Reviewers':
                pull_request_reviewers = " / ".join(
                    str(x) for x in [''.join(rev.text.split()) for rev in form_span.find_all('p')])
            elif form_span.find_all('p') and ''.join(form_div.text.split()) == 'Assignees':
                pull_request_assignees = " / ".join(
                    str(x) for x in [''.join(rev.text.split()) for rev in form_span.find_all('p')])
        user_request_result = {'user_link': user_req, 'pull_request': text,
                               'pull_request_link': link,
                               'pull_request_reviewers': pull_request_reviewers,
                               'pull_request_assignees': pull_request_assignees}
        UserRequestResult.objects.create(**user_request_result)
    return UserRequestResult.objects.filter(user_link=user_req)
