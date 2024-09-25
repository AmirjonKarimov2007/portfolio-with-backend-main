def check_click_likes(request):
    try:
        click_likes = request.session['click_likes']
    except:
        request.session['click_likes'] = []
        click_likes = request.session.get('click_likes')
        
    return click_likes


def check_read_articles(request):
    try:
        read_articles = request.session['read_articles']
    except:
        request.session['read_articles'] = []
        read_articles = request.session.get('read_articles')
        
    return read_articles
