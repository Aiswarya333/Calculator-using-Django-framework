#import json
#import math
#import pdb
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'cal/index.html')

def calc_op(request):
      return render(request, 'cal/index.html')
 
