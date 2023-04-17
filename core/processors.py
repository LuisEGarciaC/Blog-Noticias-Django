from .models import Post, About, Link, Category



# REDES SOCIALES
def ctx_dic_about(request):
    ctx_about = {}

    ctx_about['ABOUT'] = About.objects.latest('created')
    return ctx_about

# category
def ctx_dic_category(request):
    ctx_category = {}

    ctx_category['categories'] = Category.objects.filter(active=True)

    return ctx_category

# Link


def ctx_dic_link(request):
    ctx_link = {}

    links = Link.objects.all()

    for link in links:
        ctx_link[link.key] = {'url': link.url, 'icon': link.icon}

    return ctx_link



# historial de post
def ctx_dic_history(request):
    ctx_history = {}
    ctx_history['dates'] = Post.objects.dates('created', 'month').distinct()
    
    return ctx_history
