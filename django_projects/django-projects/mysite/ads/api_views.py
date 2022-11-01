import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from ads.models import Ad


def Ad_to_dict(Ad):
    result =  {
        "pk": Ad.pk,
        "title": Ad.title,
        "created_at": Ad.created_at,
        "updated_at": Ad.updated_at,
        "price": Ad.price,
        "text": Ad.text,
        "content_type" :Ad.content_type,

    }

    if Ad.picture:
        result["image"]: True
    else:
        result["image"]:False
    if Ad.favorites:
        result["favorites"]: True
    else:
        result["favorites"]:False

    return result

@csrf_exempt
def Ad_list(request):
    if request.method == "GET":
        ads = Ad.objects.all()
        ads_as_dict = [Ad_to_dict(ad) for ad in ads]
        return JsonResponse({"data": ads_as_dict})

    elif request.method == "POST":
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(**ad_data)
        return HttpResponse(
            status=HTTPStatus.CREATED,
            headers={"Location": reverse("ads:api_ad_detail", args=(ad.pk,))},
        )

    return HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def Ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)

    if request.method == "GET":
        return JsonResponse(Ad_to_dict(ad))
    elif request.method == "PUT":
        ad_data = json.loads(request.body)
        for field, value in ad_data.items():
            setattr(ad, field, value)
        ad.save()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)
    elif request.method == "DELETE":
        ad.delete()
        return HttpResponse(status=HTTPStatus.NO_CONTENT)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])



