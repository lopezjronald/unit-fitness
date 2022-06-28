from documents.models import Document


def document(request):
    document_list = Document.objects.all()
    return {"document_list": document_list}


def document_types(request):
    document_type_list = Document.objects.values("type").distinct()
    return {"document_type_list": document_type_list}