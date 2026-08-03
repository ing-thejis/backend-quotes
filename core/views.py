from rest_framework.views import APIView
from rest_framework.response import Response
from .models import QuoteModel
from .serializers import QuoteSerializer

class QuoteView(APIView):
    serializer_class = QuoteSerializer

    def get(self, request):
        detail = [
            {"name": obj.name, "detail": obj.detail}
            for obj in QuoteModel.objects.all()
        ]
        return Response(detail)

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)