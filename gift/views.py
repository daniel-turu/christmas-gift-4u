from django.shortcuts import redirect, render
from .forms import Gift_Name_Form
from .models import Gift_Name, Device
from django.utils.text import slugify
# Create your views here.




# def save(self, *args, **kwargs):

#     if self.slug == None:
#         slug = slugify(self.name)
#         has_slug = Gift_Name.objects.filter(slug=slug).exists()
#         count = 1
#         while has_slug:
#             count += 1
#             slug = slugify(self.name) + "-" + str(count)
#             has_slug = Gift_Name.objects.filter(slug=slug).exists()

#         self.slug = slug





# def home(request):

#     context={}
#     form = Gift_Name_Form()
#     context={'form':form}

#     if request.POST:
#         user = Gift_Name()
#         form = Gift_Name_Form(request.POST, instance=user)

#         if form.is_valid():
#             form.save()
            
#         return render(request, 'gift/index.html',context)
        
#     return render(request, 'gift/index.html',context)





def home(request, ):
    context={}
    
    ctm = Device.objects.get_or_create(device = request.META['HTTP_USER_AGENT'])
   

    form = Gift_Name_Form()
    
    context={'form':form}
    if request.POST:
        name = request.POST['name']
        slug = slugify(request.POST['name'])
        has_slug = Gift_Name.objects.filter(slug=slug).exists()
        count = 1
        while has_slug:
            count += 1
            slug = slugify(request.POST['name']) + "-" + str(count)
            has_slug = Gift_Name.objects.filter(slug=slug).exists()
        user = Gift_Name()
        form = Gift_Name_Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            
            context['name'] = Gift_Name.objects.get(slug=slug)
        return redirect('name',slug)
        
    return render(request, 'gift/index.html',context)



def name(request, slug):

    context={}
    form = Gift_Name_Form()
    context={'form':form}
    ctm = Device.objects.get_or_create(device = request.META['HTTP_USER_AGENT'])
    if request.POST:
        name = request.POST['name']
        slug = slugify(request.POST['name'])
        has_slug = Gift_Name.objects.filter(slug=slug).exists()
        count = 1
        while has_slug:
            count += 1
            slug = slugify(request.POST['name']) + "-" + str(count)
            has_slug = Gift_Name.objects.filter(slug=slug).exists()
        user = Gift_Name()
        form = Gift_Name_Form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            
            context['name'] = Gift_Name.objects.get(slug=slug)
        return redirect('name',slug)

    context['name'] = Gift_Name.objects.get(slug=slug)
    context['link'] = Gift_Name.objects.get(slug=slug)

    return render(request, 'gift/index.html',context)




# def firstform(request, *args, **kwargs):
#     context = {}
#     user = request.user
#     form = account_for_Form(instance=user)
#     if request.method == 'POST':
#         user = account_for(user=request.user)
#         form = account_for_Form(request.POST, instance=user)
#         if form.is_valid():

#             form.save()
#             acounttypte = form.cleaned_data.get('account_type')
#             blog = form.cleaned_data.get('Blogging')
#             if acounttypte == "None":
#                 messages.info(request, f"You have sucessfully signin for .")
#             else:
#                 messages.info(request, f"You have sucessfully signin for .")
                
#             messages.info(request, f"You have sucessfully signin for .")
#             return redirect("business")
#     context={'form':form,}
#     return render(request, 'business_handwork/First_form_display.html',context)