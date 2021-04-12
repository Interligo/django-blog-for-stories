from django.test import TestCase
from django.utils.timezone import now

from stories.models import Story
from stories.models import Comment


class TestStoryModel(TestCase):
    def setUp(self) -> None:
        self.test_story1 = Story.objects.create(
            story_title='Заголовок',
            story_text='Текст'
        )
        self.test_story2 = Story.objects.create(
            story_title='Заголовок рассказа',
            story_text='Текст рассказа',
            story_competition='Наименование конкурса',
            story_competition_description='Описание конкурса',
            story_award_winning_place='I'
        )

    def test_story1_title(self) -> None:
        self.assertEqual(self.test_story1.story_title, 'Заголовок')

    def test_story1_text(self) -> None:
        self.assertEqual(self.test_story1.story_text, 'Текст')

    def test_story1_competition(self) -> None:
        self.assertEqual(self.test_story1.story_competition, 'Неизвестно')

    def test_story1_competition_description(self) -> None:
        self.assertEqual(self.test_story1.story_competition_description, 'Неизвестно')

    def test_story1_award_winning_place(self) -> None:
        self.assertEqual(self.test_story1.story_award_winning_place, 'Неизвестно')

    def test_story2_title(self) -> None:
        self.assertEqual(self.test_story2.story_title, 'Заголовок рассказа')

    def test_story2_text(self) -> None:
        self.assertEqual(self.test_story2.story_text, 'Текст рассказа')

    def test_story2_competition(self) -> None:
        self.assertEqual(self.test_story2.story_competition, 'Наименование конкурса')

    def test_story2_competition_description(self) -> None:
        self.assertEqual(self.test_story2.story_competition_description, 'Описание конкурса')

    def test_story2_award_winning_place(self) -> None:
        self.assertEqual(self.test_story2.story_award_winning_place, 'I')


class TestCommentModel(TestCase):
    def setUp(self) -> None:
        self.test_story1 = Story.objects.create(
            story_title='Заголовок1',
            story_text='Текст1'
        )
        self.test_story2 = Story.objects.create(
            story_title='Заголовок2',
            story_text='Текст2'
        )
        self.test_comment = Comment.objects.create(
            story=self.test_story1,
            authors_name='Автор комментария',
            comment_text='Текст комментария',
            publication_date=now()
        )

    def test_is_comment_belong_to_story1(self) -> None:
        self.assertEqual(str(self.test_comment.story), 'Заголовок1')

    def test_is_comment_belong_to_story2(self) -> None:
        self.assertNotEqual(str(self.test_comment.story), 'Заголовок2')

    def test_comment_author(self) -> None:
        self.assertEqual(self.test_comment.authors_name, 'Автор комментария')

    def test_comment_text(self) -> None:
        self.assertEqual(self.test_comment.comment_text, 'Текст комментария')
