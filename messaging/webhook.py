from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def message_received(request):
    if request.method == "POST":
        print("received message", request.data)
        return Response(
            {"success": True, "message": "success", "data": "none"},
            status=status.HTTP_200_OK,
        )
