from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Función para crear paginación
def get_paginated(request, queryset, page_number):
    # Divide en página de 10 objectos
    paginator = Paginator(queryset, page_number)
    page_number = request.query_params.get('page', 1)

    try:
        # Obtener la página solicitada
        queryset = paginator.page(page_number)

    except PageNotAnInteger:
        # Número de página no es un entero
        queryset = paginator.page(1)

    except EmptyPage:
        # Página fuera del rango
        queryset = paginator.page(paginator.num_pages)
    
    return queryset
