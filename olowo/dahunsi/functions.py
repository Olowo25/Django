def upload(f):
    with open('dahunsi/templates/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
