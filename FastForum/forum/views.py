from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Thread, Comment 
from .forms import ThreadForm, CommentForm

from django.http import HttpResponse 

def index(request):
		form = ThreadForm
		
		if request.method == 'POST':
			form_info = form(data=request.POST)
    			title = request.POST.get('title', '')
    			content = request.POST.get('content', '')
    			t = Thread(title=title, description = content,
				pub_date = timezone.now(), upvotes = 0)
			t.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/' + str(len(Thread.objects.filter())+1))


		return render(request, 'forum/index.html', {'form': form,})

def thread(request, thread_id):
		try: 
			thread1 = Thread.objects.get(pk=thread_id)
		except Thread.DoesNotExist:
			raise Http404("Thread does not exist!")

		form = CommentForm
		if request.method == 'POST':
			form_info = form(data=request.POST)
			submission = request.POST.get('content', '')
			c = Comment(text=submission, pub_date = timezone.now(), upvotes = 0,
				thread=thread1)
			c.save()
			return HttpResponseRedirect('http://127.0.0.1:8000/' + str(thread_id))

		return render(request, 'forum/thread.html', {'thread':thread1, 'form':form,})