from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.timezone import now
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Story
from .forms import LeaveCommentForm
from .serializers import StoryDetailSerializer
from .serializers import StoriesListSerializer
from .serializers import StoryDetailTextSerializer
from analytics.models import PageHit
from analytics.decorators import counted


def index(request):
    """All stories list."""
    all_stories = Story.objects.all()
    return render(request, 'stories/stories_list.html', {'all_stories': all_stories})


@counted
def detail(request, story_id):
    """Current story detail."""
    story = get_object_or_404(Story, id=story_id)
    comments = story.comments.order_by('-id')
    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    form = LeaveCommentForm()

    try:
        comments_on_page = paginator.page(page)
    except PageNotAnInteger:
        comments_on_page = paginator.page(1)
    except EmptyPage:
        comments_on_page = paginator.page(paginator.num_pages)

    views = PageHit.objects.get(id=story_id)

    return render(request, 'stories/story_detail.html', {'story': story,
                                                         'comments': comments,
                                                         'comments_on_page': comments_on_page,
                                                         'views': views,
                                                         'form': form})


def leave_comment(request, story_id):
    """Current story comments creator."""
    story = get_object_or_404(Story, id=story_id)
    story.comments.create(authors_name=request.POST['author'],
                          comment_text=request.POST['text'],
                          publication_date=now())
    return HttpResponseRedirect(reverse('stories:detail', args=(story.id,)))


class StoryCreateView(generics.CreateAPIView):
    """Story creation for admins by API."""
    serializer_class = StoryDetailSerializer
    permission_classes = (IsAdminUser,)


class StoriesListView(generics.ListAPIView):
    """Stories list for all by API"""
    serializer_class = StoriesListSerializer
    queryset = Story.objects.all()


class StoryChangeView(generics.RetrieveUpdateDestroyAPIView):
    """Stories change for admins by API."""
    serializer_class = StoryDetailSerializer
    queryset = Story.objects.all()
    permission_classes = (IsAdminUser,)


class StoryDetailView(generics.RetrieveAPIView):
    """Story detail for all by API."""
    serializer_class = StoryDetailTextSerializer
    queryset = Story.objects.all()
