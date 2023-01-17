from storage_5d_pr.models import Construction


def data_to_base(request):
    construcitons = Construction.objects.all()
    context = {
        'constructions': construcitons
    }
    return context
