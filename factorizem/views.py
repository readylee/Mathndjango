from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

class FactorizemView(TemplateView):

    template_name = "factorizem/index.html"
    init_context = {'target': '', 'errormsg': None, 'factors': None, 'prime': False}

    INVALID_VALUE_ERR_MSG = "Please provide an integer value."
    SUBZERO_VALUE_ERR_MSG = "Please provide a positive integer."

    MIN_INT_VAL = 1

    def post(self, request):
        context = self.init_context
        if request.POST.get('num'):
            context['factors'] = None
            context['errormsg'] = None
            context['prime'] = None
            num = request.POST.get('num')
            context['target'] = num
            try:
                # cast to int, maybe
                intNum = int(num)
                if intNum < self.MIN_INT_VAL:
                    context['errormsg'] = self.SUBZERO_VALUE_ERR_MSG
                else:
                    factors = self.find_positive_factors(self.MIN_INT_VAL, intNum)
                    context['factors'] = factors
                    if factors and len(factors) < 3:
                        context['prime'] = True 
            except ValueError:
                context['errormsg'] = self.INVALID_VALUE_ERR_MSG
        return render(request, self.template_name, context)
    
    def find_positive_factors(self, minFactor, targetVal):
        factorsList = []
        for i in range(minFactor, targetVal):
            if targetVal % i == 0:
                factorsList.append(i)
        factorsList.append(targetVal)
        return factorsList



