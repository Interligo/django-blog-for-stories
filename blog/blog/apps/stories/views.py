from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.timezone import now

from .models import Story
from .models import Comment
from analytics.models import PageHit
from analytics.decorators import counted


def index(request):
    all_stories = Story.objects.all()
    return render(request, 'stories/stories_list.html', {'all_stories': all_stories})


@counted
def detail(request, story_id):
    try:
        story = Story.objects.get(id=story_id)
    except:
        raise Http404('Ничего найти не удалось!')

    comments = story.comment_set.order_by('-id')
    views = PageHit.objects.get(id=story_id)

    return render(request, 'stories/story_detail.html', {'story': story, 'comments': comments, 'views': views})


# TODO: проверить приходит ли post запрос
def leave_comment(request, story_id):
    try:
        story = Story.objects.get(id=story_id)
    except:
        raise Http404('Ничего найти не удалось!')

    story.comment_set.create(authors_name=request.POST['comment_author_name'],
                             comment_text=request.POST['comment_text'],
                             publication_date=now())

    return HttpResponseRedirect(reverse('stories:detail', args=(story.id,)))
