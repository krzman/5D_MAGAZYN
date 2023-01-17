from storage_5d_pr.models import Construction


def data_to_base(request):
    construciton = Construction.objects.all()
    context = {
        'construction': construciton
    }
    return context
