def check_click_likes(request):
    try:
        click_likes = request.session['click_likes']
    except:
        request.session['click_likes'] = []
        click_likes = request.session.get('click_likes')
        
    return click_likes
