from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Topic, Comment
from django.http import HttpResponseRedirect

# Create your views here.

class Home(generic.ListView):
    template_name = 'home.html'
    model = Topic
    # paginate_by = 7


class TopicView(generic.DetailView):
    model = Topic
    template_name = 'topicView.html'


class TopicCreate(generic.edit.CreateView):
    model = Topic
    fields = ['title', 'text']
    success_url = '/'


    def form_valid(self, form):
        form.instance.user = self.request.user
        #success_url = '/topic/'+Topic.objects.get()

        return super().form_valid(form)

# 04 May 2019 added. This is to create add comments page
class CommentCreate(generic.edit.CreateView):
    model = Comment
    fields = ['text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
# End of this block

def vote(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.POST['vote'] == '+':
        comment.vote +=1
        print(f"Vote +1 comment {comment.id}")
    elif request.POST['vote'] == '-':
        comment.vote -=1
        print(f"Vote -1 comment {comment.id}")

    comment.save()
    return redirect('adviseMeApp:topicview',pk=comment.topic_id)
