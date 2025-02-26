from django.http import JsonResponse
from .models import UserDetails 

def get_all_users(request):
    users = list(UserDetails.objects.values())  
    return JsonResponse(users, safe=False)

def get_user_by_email(request, email):
    user = UserDetails.objects.filter(email=email).values().first()  
    if user:
        return JsonResponse(user, safe=False)
    return JsonResponse({'error': 'User not found'}, status=404)  

def delete_user(request, email):
    deleted_count, _ = UserDetails.objects.filter(email=email).delete() 
    if deleted_count:
        return JsonResponse({'message': 'User deleted successfully'})
    return JsonResponse({'error': 'User not found'}, status=404)  
