import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from hesabyar.models import User, Contact, Transaction, TransactionMember


@csrf_exempt
def index(request):
    return JsonResponse({"status": "Salam! I'm OK!"})


@csrf_exempt
def login(request):
    try:
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            return JsonResponse({'user': user.pk})
        else:
            return JsonResponse({"status": "error", "msg": "user not found"}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})


@csrf_exempt
def get_contacts(request):
    try:
        return JsonResponse(
            json.loads((serializers.serialize("json", Contact.objects.filter(user=request.POST['user'])))), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})


@csrf_exempt
def get_transactions(request):
    try:
        return JsonResponse(
            json.loads((serializers.serialize("json", Transaction.objects.filter(user=request.POST['user'])))),
            safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})


@csrf_exempt
def add_transaction(request):
    try:
        tran = Transaction(user=User.objects.get(pk=request.POST['user']), amount=request.POST['amount'],
                           category=request.POST['category'])
        tran.save()
        for item in request.POST['members']:
            member = TransactionMember(transaction=tran, member=User.objects.get(pk=item))
            member.save()
        return JsonResponse({"status": "ok"})
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})


@csrf_exempt
def delete_transaction(request):
    try:
        tran = Transaction.objects.get(pk=request.POST['transaction'])
        tran.delete()
        return JsonResponse({"status": "ok"})
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})


@csrf_exempt
def edit_transaction(request):
    try:
        tran = Transaction.objects.get(pk=request.POST['transaction'])
        tran.amount = request.POST['amount']
        tran.category = request.POST['category']
        tran.save()
        TransactionMember.objects.filter(transaction=1).delete()
        for item in request.POST['members']:
            member = TransactionMember(transaction=tran, member=User.objects.get(pk=item))
            member.save()
        return JsonResponse({"status": "ok"})
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})
