from django.shortcuts import render
from django.http import JsonResponse
from .models import Category

# Create your views here.

def index(request):
    '''
    First page that gets loaded

    Parameter:
        Incoming HTTP Request
    Returns:
        HttpResponse response with context dictionary
    '''
    root_categories = get_root_categories()
    return render(request, 'index.html', context=root_categories)
    


def get_root_categories():
    '''
    Creates the root categories
     
    Returns: dictionary of root categories 
    '''
    
    create_categories(['A', 'B'], True)
    root_categories_result = Category.objects.filter(parent_id__isnull=True)
    root_categories = {'categories':[]}           
    if root_categories_result.exists(): 
        for cat in root_categories_result:
            root_categories['categories'].append(
                                        {'id': cat.category_id, 'name': cat.category_name})
   
    return root_categories



def create_categories(cat_list, is_root=False):
    '''
    Creates the children of given categories

    Parameter:
        list of categories
        is_root: should be True if root categories to be created.
    '''
   
    cat_id = ''
    p_id = None
    cat_name = ''
    no_of_children = 2

    if is_root:
        Category.objects.all().delete()
        for category in cat_list:
            cat_id = category
            p_id = None
            cat_name = '.Category '+category
            Category.objects.create(category_id=cat_id, category_name=cat_name, parent_id=p_id)
    else:
        for id in cat_list:
            result = Category.objects.filter(category_id=id)
            for r in result:
                for i in range(1,no_of_children+1):
                    cat_id = r.category_id + '-'+str(i)
                    cat_name = '.SUB '+ r.category_name.lstrip(".")+'-'+str(i)
                    Category.objects.create(
                                    category_id=cat_id, category_name=cat_name, parent_id=id)



def get_child(request):
    '''
    Gets the children of selected checkbox 

    Parameter:
        Incoming HTTP Request

    Returns:
        JsonResponse with child list of selected checkbox 
    '''
    
    if request.method == 'GET':
        data = request.GET.get('parent')
        if data is not None:
            result = Category.objects.filter(parent_id=data)
            child_list = []
            if  not result.exists():
                create_categories([data])
                result = Category.objects.filter(parent_id=data)
    
            for r in result:
                child_list.append({'id':r.category_id, 'name': r.category_name})
        
    return JsonResponse(child_list, safe=False)



def get_all_children(request):
    '''
    Gets nested children of deselected checkbox 

    Parameter:
        Incoming HTTP Request

    Returns:
        JsonResponse with nested children of deselected checkbox 
    '''
    children_list = []
    if request.method == 'GET':
        pid = request.GET.get('parent')
        children_list = get_nested_children(pid)
        # pid = request.GET.get('parent')
        #remove the unchecked checkbox from the list
        children_list = [d for d in children_list if d['id'] != pid]
    return JsonResponse(children_list, safe=False)
    


def get_nested_children(pid):
    '''
    Resursive Function to get nested children 

    Parameter:
        parent category id

    Returns:
        child list 
    '''
    child_list = []
    child_list.append({'id':pid})
    result = Category.objects.filter(parent_id=pid)
    sub_list = []
    if result.exists():
        for r in result:
            # sub_list.append(get_nested_children(r.category_id))
            sub_list += get_nested_children(r.category_id)
    if len(sub_list) > 0:
        # child_list.append(sub_list)
        child_list += sub_list
    return child_list
   