from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone
# Create your tests here.
from .models import Course, Step


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python",
            description="Learn to write REGEX"
        )
        now = timezone.now()
        self.assertLessEqual(course.created_at, now)


class StepModelSteps(TestCase):
    def test_step_creation(self):
        step = Step.objects.create(
            title="Doing a test step",
            description="Learn to test",
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())


# Create some content for us and test it
class CourseViewTests(TestCase):
    # content
    def setUp(self):
        self.course = Course.objects.create(
            title="Python testing",
            description="New tests"
        ),
        self.course2 = Course.objects.create(
            title="Python checking",
            description="New checks"
        ),
        self.step = Step.objects.create(
            titles="Introduction to Doctests",
            description="Learn to write tests",
            course=self.course
        )

    # testing
    def test_course_list_view(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['counrses'])
