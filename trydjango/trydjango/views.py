from django.http import HttpResponse


from articles.models import Article

def home(request):
    """[home view]

    Args:
        request ([type]): [description]
        request argument is the request sent by django

        Return HTML as a response
    """
    article_obj = Article.objects.get(id=2)

    HTML_STRING = f"""
    <h1>Hello World!</h1>
    <h1>{ article_obj.title }(id: { article_obj.id })</h1>
    <p>{ article_obj.content }!</p>
    """
    return HttpResponse(HTML_STRING)