from django.shortcuts import render

def home(request):
    default_template = 'sample/sample.html'
    templates = {
        'A': 'blog/blog_sample1.html',
        'B': 'blog/blog_sample2.html',
    }
    template_type = request.GET.get('type')
    template = templates.get(template_type, default_template)
    return render(request, template)

