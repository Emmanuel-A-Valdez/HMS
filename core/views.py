from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# CLASE QUE LISTA LAS URLS
class ListUrls(APIView):
    """
    Return a list of all developer related urls.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):

        urls = {
            # Users
            "Urls": "",
            "Register": "account/register/",
            # "Email Verification": "verify-email/",
            # "Resend Email Verification": "resend-verification/",
            "Login": "account/login/",
            "Logout": "account/logout/",
            "User detail - Update": "account/user/",
            "Change Password": "account/password/change/",
            "Request Password Reset": "account/request-password-reset/",
            "Password Reset Confirmation": "account/reset-password/",
            "*": "------------------------------------------------------------",
            # Developers
            "Developers": "developer/",
            "Developer": "developer/details/",
            "Dev search": "developer/search/<int:id>/",
            "Dev Achievements": "developer/achievements/",
            "Dev Achievement": "developer/achievements/<int:pk>/",
            "Dev Achievement": "developer/achievements-public/<int:pk>/",
            "Achievements from contacts": "developer/feed/",
            "Achievements random": "developer/feed/random/",
            "Like Achievement": "developer/like/<int:pk>/",
            "**": "------------------------------------------------------------",
            # Company
            "Companies": "company/",
            "Company": "company/detail/",
            "Company search": "company/search/<int:id>/",
            "Job openings": "company/job-listing/",
            "Job opening:": "company/job-listing<int:pk>/",
            "Job opening public:": "company/job-listing-public/<int:pk>/",
            "Feed of jobs opening randomly": "company/listings-feed/random/",
            "Feed of jobs opening from companies followed": "company/listings-feed/followed/",
            "Like Job Opening": "company/like/<int:pk>/",
            "***": "------------------------------------------------------------",
            # Invite
            "Invite": "invite/",
            "Refs": "invite/refs/",
            "****": "------------------------------------------------------------",
            # Match and searches.
            "Manual search": "match/search/",
            "Dev match": "match/dev/",
            "Dev match detail": "match/dev/<int:pk>/",
            "Dev match status": "match/dev/status/<int:status>",
            "Job match": "match/jobs/<int:pk>/",
            "Job match detail": "match/jobs/<int:pk>/detail/<int:dk>/",
            "Job match status": "match/jobs/<int:pk>/status/<int:status>/",
            "Job search": "match/search_jobs/?search=<str>+<str>",
            "Job advanced search": "match/search_jobs/?frameworks=<str>&technologies=<str>",
            "Developer search": "match/search_devs/?search=<str>+<str>",
            "Developer advanced search": "match/search_devs/?location=<str>&dev_area=<str>",
            "Live search": "match/live_search/",
            "*****": "------------------------------------------------------------",
            # Connect
            "Friend Requests": "connect/friend/requests/",
            "Send a friend request": "connect/send/request/<int:id>/",
            "Friend request options": "connect/request/options/<int:id>/<int:option>/",
            "List of friends": "connect/friends/",
            "Delete friend": "connect/unfriend/<int:id>/",
            "Mutual friend or follow request sended or send a request": "connect/mutual/friends/<int:id>/",
            "Companies following list": "connect/following/",
            "Follow company": "connect/follow/<int:id>/",
            "Unfollow company": "connect/unfollow/<int:id>/",
            "Follow or unfollow company": "connect/followed/<int:id>/",
            "Followers list": "connect/followers/",
            "***": "------------------------------------------------------------",
            # Chat threads.
            "Developers thread list": "chat/",
            "Developers thread creation": "chat/create/thread/",
            "Developers thread detail": "chat/thread/<int:pk>/",
            "Match thread list": "chat/match/",
            "Match thread creation": "chat/match/create/thread",
            "Match thread detail": "chat/match/thread/<int:pk>/",
            "Messages List": "chat/thread/messages/<int:pk/",
            # Notifications
            "See Notifications": "notification/",
            "See/Delete Notification": "notification/<int:pk>/",
            "Websockets": "------------------------------------------------------------",
            "Notifications": "ws/notifications/<str:token>/",
            "Thread(All chats)": "ws/thread/<str:token>/",
            "Enter chat": "ws/chat/<str:token>/<int:chat>/",
        }
        return Response(urls, status=status.HTTP_200_OK)
