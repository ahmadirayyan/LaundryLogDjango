from laundrylog.response import Response
from . import transformer
from .models import Items
import json
from django.views.decorators.csrf import csrf_exempt
from laundrylog.middleware import jwtRequired

# Create your views here.
@csrf_exempt
@jwtRequired
def index(request):
    if request.method == 'GET':
        item = Items.objects.all()
        item = transformer.transform(item)
        return Response.ok(item)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        item = Items()
        item.category = json_data['category']
        item.color = json_data['color']
        item.brand = json_data['brand']
        item.price = json_data['price']
        item.desc = json_data['desc']
        item.status = json_data['status']
        item.datebought = json_data['datebought']
        item.save()
        return Response.ok(
            values = transformer.singleTransform(item),
            message = 'Item created'
        )

@csrf_exempt
@jwtRequired
def show(request, id):
    if request.method == 'GET':
        item = Items.objects.filter(id=id).first()
        if not item:
            return Response.badRequest(message='Item not found')
        item = transformer.transform(item)
        return Response.ok(values=item)
    elif request.method == 'PUT':
        item = Items.objects.filter(id=id).first()
        if not item:
            return Response.badRequest(message='Item not found')
        json_data = json.loads(request.body)
        item.category = json_data['category']
        item.color = json_data['color']
        item.brand = json_data['brand']
        item.price = json_data['price']
        item.desc = json_data['desc']
        item.status = json_data['status']
        item.datebought = json_data['datebought']
        item.save()
        return Response.ok(
            values = transformer.singleTransform(item),
            message = 'Item updated'
        )
    elif request.method == 'DELETE':
        item = Items.objects.filter(id=id).first()
        if not item:
            return Response.badRequest(message='Item not found')
        item.delete()
        return Response.ok(
            message = 'Item deleted'
        )
    else:
        return Response.badRequest(message='Uhh... We don\'t serve that')