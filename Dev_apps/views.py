# from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
# from django.contrib import messages
# from django.views import generic
from django.contrib.auth.decorators import login_required
# from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import *
from .forms import *


# Create your views here.
