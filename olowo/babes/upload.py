def upload(f):
    with open('babes/templates/uploads/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
