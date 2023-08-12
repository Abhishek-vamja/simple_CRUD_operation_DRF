"""
View for student api.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from core.models import *
from core.serializers import *


class StudentListAPI(APIView):
    """
    For handle listing and creating students.
    """

    def get(self,request):
        """List all students."""
        
        std = Student.objects.all()
        serializer = StudentSerializer(std,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        """Creating students."""

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Data':serializer.data},status=status.HTTP_201_CREATED)
        
        return Response({'Error':serializer.errors})


class StudentDetailAPI(APIView):
    """
    For handle listing , updating students by ids.
    """

    def get(self,request,pk):
        """Show student by their id."""

        std = Student.objects.get(pk=pk)
        serializer = StudentSerializer(std)

        return Response({'Data':serializer.data})
    
    def put(self,request,pk):
        """Update all fields of student."""

        std = Student.objects.get(pk=pk)
        serializer = StudentSerializer(std,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Data':serializer.data},status=status.HTTP_200_OK)
        
        return Response({'Error':serializer.errors})
    
    def patch(self,request,pk):
        """Update fields partially of student."""

        std = Student.objects.get(pk=pk)
        serializer = StudentSerializer(std,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'Data':serializer.data},status=status.HTTP_200_OK)
        
        return Response({'Error':serializer.errors})
    
    def delete(self,request,pk):
        """Delete student from database."""

        std = Student.objects.get(pk=pk)
        std.delete()

        return Response({'Message':'Deleted successfully!!',},status=status.HTTP_204_NO_CONTENT)