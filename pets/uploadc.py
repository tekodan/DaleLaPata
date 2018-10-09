def import_csv(request):

    file = './data/cities_data/brazil'
    with open(file, 'rb') as csvfile:
          with closing(connections['pets'].cursor()) as cursor:
                cursor.copy_from(
                    file=csvfile,
                    table='cities_city', #<-- table name from db
                    sep='|',  #<-- delimiter
                    columns=(
                        'oil_share',
                        'gas_share',
                        'growth',
                        'capex_to_cf',
                        ... etc.
                    ),
            )

    return HttpResponse('Done!')
