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
    user = authenticate(username=request['user'], password=request['pass'])
    if user is not None:
        return JsonResponse(
            json.loads((serializers.serialize("json", user))), safe=False)
    else:
        return JsonResponse({"status": "error"})


@csrf_exempt
def get_contacts(request):
    try:
        return JsonResponse(
            json.loads((serializers.serialize("json", Contact.objects.filter(user=request.body['user'])))), safe=False)
    except:
        return JsonResponse({"status": "error"})


@csrf_exempt
def get_transactions(request):
    try:
        return JsonResponse(
            json.loads((serializers.serialize("json", Transaction.objects.filter(user=request.body['user'])))),
            safe=False)
    except:
        return JsonResponse({"status": "error"})


@csrf_exempt
def add_transaction(request):
    try:
        tran = Transaction(user=User.objects.get(pk=request.body['user']), amount=request.body['amount'],
                           category=request.body['category'])
        tran.save()
        for item in request.body['members']:
            member = TransactionMember(transaction=tran, member=User.objects.get(pk=item['user']))
            member.save()
        return JsonResponse({"status": "ok"})
    except:
        return JsonResponse({"status": "error"})


@csrf_exempt
def delete_transaction(request):
    try:
        tran = Transaction.objects.get(pk=request.body['transaction'])
        tran.delete()
        return JsonResponse({"status": "ok"})
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"})


@csrf_exempt
def edit_transaction(request):
    try:
        tran = Transaction.objects.get(pk=request.body['transaction'])
        tran.amount = request.body['amount']
        tran.category = request.body['category']
        tran.save()
        TransactionMember.objects.filter(transaction=1).delete()
        for item in request.body['members']:
            member = TransactionMember(transaction=tran, member=User.objects.get(pk=item['user']))
            member.save()
        return JsonResponse({"status": "ok"})
    except:
        return JsonResponse({"status": "error"})
