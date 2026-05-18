from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', type='run', duration=10)
        self.assertEqual(activity.type, 'run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='testuser', score=50)
        self.assertEqual(lb.score, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushup', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')
