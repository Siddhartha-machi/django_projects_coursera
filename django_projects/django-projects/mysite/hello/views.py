from django.http import HttpResponse
# Create your views here.

def myview(request):

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    resp = HttpResponse("view count="+str(request.session['num_visits']))
    resp.set_cookie('dj4e_cookie', 'b4b6a468', max_age=1000)


    return resp