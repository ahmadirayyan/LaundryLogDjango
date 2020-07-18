from laundrylog.response import Response
from . import transformer
from .models import Users
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from laundrylog.jwt import JWTAuth
from laundrylog.middleware import jwtRequired

# Create your views here.
def auth(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        email = json_data['email']
        user = Users.objects.filter(email=email).first()
        if not user:
            return Response.badRequest(message='User not found')
        if not check_password(json_data['password'], user.password):
            return Response.badRequest(message='Wrong email and password combination')
        user = transformer.singleTransform(user)
        jwt = JWTAuth()
        user['token'] = jwt.encode({'id': user['id']})
        return Response.ok(values=user, message='Login success')

@jwtRequired
def index(request):
    if request.method == 'GET':
        user = Users.objects.all()
        user = transformer.transform(user)
        return Response.ok(values=user)
    elif request.method == 'POST':
        json_data = json.loads(request.body)
        user = Users()
        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()
        return Response.ok(
            values = transformer.singleTransform(user),
            message = 'User created'
        )

@jwtRequired
def show(request, id):
    if request.method == 'GET':
        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message='User not found')
        user = transformer.singleTransform(user)
        return Response.ok(values=user)
    elif request.method == 'PUT':
        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message='User not found')
        json_data = json.loads(request.body)
        user.name = json_data['name']
        user.email = json_data['email']
        user.password = make_password(password=json_data['password'])
        user.save()
        return Response.ok(
            values = transformer.singleTransform(user),
            message = 'User updated'
        )
    elif request.method == 'DELETE':
        user = Users.objects.filter(id=id).first()
        user = Users.objects.filter(id=id).first()
        if not user:
            return Response.badRequest(message='User not found')
        user.delete()
        return Response.ok(
            message='User deleted'
        )
    else:
        return Response.badRequest(message='Uhh... We don\'t serve that')