import json
from json import JSONDecodeError, loads

from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import UserProfile


# Create your views here.

@csrf_exempt
def login(request) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": f"{request.method} method not allowed."}, status=405)

    try:
        data = loads(request.body)
        email = data.get("email")
        password = data.get("password")
        print(f"{email}, {password}")
        if not email or not password:
           return JsonResponse({"error": "Email and password are required."}, status=400)
        try:

            user_object = UserProfile.objects.get(email=email)
            username = user_object.username
        except UserProfile.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=400)


        user_object = authenticate(username=user_object.username, password=password)

        if user_object is not None:
            return JsonResponse(
                {
                    'uid' : user_object.id,
                    'username' : username,
                },
                status=200
            )
        else:
            return JsonResponse({"error": "Invalid credentials."}, status=404)

    except JSONDecodeError:
        return JsonResponse({"error": "Cannot process json data."}, status=400)


@csrf_exempt
def register(request) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"error": f"{request.method} not allowed'"}, status=405)

    try:
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        address = data.get("address")
        phone = data.get("phone_number")

        user = UserProfile.objects.filter(email=email).first()

        if user is not None:
            return JsonResponse({"error": "User already exists."}, status=400)

        if password != confirm_password:
            return JsonResponse({"error": "Password do not match."}, status=400)

        #
        user = UserProfile.objects.create(
            username=username,
            email=email,
            password=password,
            phone_number=phone,
            address=address,
            is_staff=False,
        )
        user.save()
        return JsonResponse({"user_id": user.pk}, status=200)

    except JSONDecodeError:
        return JsonResponse({"error": "Cannot process json data."}, status=400)

    except Exception as e:
        return JsonResponse({"error": e.__str__()}, status=405)