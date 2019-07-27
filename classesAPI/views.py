from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from classes.models import Classroom

from .serializers import RegistrationSerializer, ClassUpdateSerializer, ClassUpdateSerializer, ClassDetailSerializer

# Create your views here.
class Registration(CreateAPIView):
	serializer_class = RegistrationSerializer 

	# def get_serializer_class(self):
 #    	if self.request.user.is_staff:
 #        	return FullAccountSerializer
 #    	return BasicAccountSerializer

# class UserLoginAPIView(APIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         my_data = request.data
#         serializer = LoginSerializer(data=my_data)
#         if serializer.is_valid(raise_exception=True):
#             valid_data = serializer.data
#             return Response(valid_data, status=HTTP_200_OK)
#         return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class ClassroomDetailAPI(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassUpdateSerializer
	lookup_id = 'id'
	lookup_url_kwarg = 'classroom_id'


class ClassroomCreateAPI(CreateAPIView):
	serializer_class = ClassDetailSerializer
	permission_classes = [IsAuthenticated]
	def perform_create(self, serializer):
		serializer.save(teacher = self.request.user)

class ClassroomUpdateAPI(RetrieveAPIView):
	serializer_class = ClassUpdateSerializer
	lookup_id = 'id'
	lookup_url_kwarg = 'class_id'
	permission_classes = [IsAuthenticated]


class ClassroomDeleteAPI(DestroyAPIView):
	lookup_id = 'id'
	lookup_url_kwarg = 'classroom_id'
	permission_classes = [IsAuthenticated]