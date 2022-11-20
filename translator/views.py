from django.shortcuts import render
from django.views import generic
from . import baidu_translate


# Create your views here.
def translator_view(request):
    if request.method == 'POST': # 有信息提交的时候
        original_text = request.POST['my_textarea']
        output = baidu_translate.baiduTranslate(original_text)
        return render(request,'translator.html',{'original_text':original_text,'output_text':output})
    else: # 没有提交的时候 method是get方法 
        return render(request,'translator.html')





