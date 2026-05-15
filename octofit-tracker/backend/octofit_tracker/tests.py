from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(username='testuser', team=team)
        self.assertEqual(str(user), 'testuser')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(username='testuser', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5.0)
        self.assertEqual(str(activity), 'testuser - run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(username='testuser', team=team)
        workout = Workout.objects.create(user=user, description='Pushups', completed=True)
        self.assertEqual(str(workout), 'testuser - Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team - 100')
