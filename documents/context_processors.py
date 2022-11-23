from documents.models import Document


def document(request):
    document_list = Document.objects.all().order_by("title")
    return {"document_list": document_list}


def document_types(request):
    document_type_list = Document.objects.values("type").distinct().order_by("type")
    return {"document_type_list": document_type_list}