from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UserProfile


@login_required
def profile(request):
	current_user = {'user': request.user}
	return render(request, 'profiles/profile.html', current_user)
