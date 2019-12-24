from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return JsonResponse({"status": "Salam"})


@csrf_exempt
def get_contacts(request):
    return JsonResponse({"status": "Salam"})


@csrf_exempt
def get_transactions(request):
    return JsonResponse({"status": "Salam"})


@csrf_exempt
def add_transaction(request):
    return JsonResponse({"status": "Salam"})


@csrf_exempt
def delete_transaction(request):
    return JsonResponse({"status": "Salam"})


@csrf_exempt
def edit_transaction(request):
    return JsonResponse({"status": "Salam"})
