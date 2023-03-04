from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse



from .models import Member
from .serializers import MemberSerializer

@api_view(['POST'])
def create_member(request):
    data = request.data
    member = Member.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        dob = data['dob'],
        phone = data['phone'],
        occupation = data['occupation'],
        membership = data['membership'],
        address = data['address'],
        department = data['department'],
        gender = data['gender'],
        profile_img = data['profile_img'] 
    )
    # member.save()
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data)

    # serializer_class = MemberSerializer
    # pagination_class = PageNumberPagination

    # def get_queryset(self):
    #     page = int(self.request.query_params.get('page', 1))
    #     return Member.objects.all().order_by('id')[page*10-10:page*10]

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     return Response(serializer.data)

# Create your views here.
@api_view(['GET'])
def get_members(request): 
    member = Member.objects.all()
    serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)


def check_email_exists(request, email):
    member = Member.objects.filter(email=email).exists()
    return JsonResponse({'success': member})

def check_phone_exists(request, phone):
    member = Member.objects.filter(phone=phone).exists()
    return JsonResponse({'success': member})




