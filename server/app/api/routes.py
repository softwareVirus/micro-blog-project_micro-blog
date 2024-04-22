from flask_restful import Api
from server.app.resources.auth import (
    LoginResource,
    SignupResource,
    LogoutResource,
    RefreshResource,
)
from server.app.resources.tag import TagResource
from server.app.resources.comment import CommentResource
from server.app.resources.post import PostResource
from server.app.resources.protected import Profile
from server.app.resources.vote import VoteResource
from server.app.resources.follow import FollowResource
from server.app.models.revoked_token import RevokedToken
from server.app.resources.conversation import Conversation
from flask import Blueprint

routes_bp = Blueprint("routes", __name__)

errors = {
    "ExpiredSignatureError": {
        "message": "Unauthorized",
        "status": 401,
    },
}

api = Api(routes_bp, errors=errors)
# Define API routes and associate them with the respective resources
api.add_resource(
    CommentResource,
    "/posts/<string:post_id>/comments",
    "/posts/<string:post_id>/comments/<string:comment_id>",
)
api.add_resource(VoteResource, "/vote/<string:post_id>")
api.add_resource(FollowResource, "/follow/<string:user_id>")
api.add_resource(
    PostResource,
    "/posts",
    "/posts/<string:tags>",
    "/post/<string:post_id>",
    "/feed_posts",
    "/user_posts/<string:user_id>",
    "/user_posts/<string:user_id>/<string:tags>",
)
api.add_resource(SignupResource, "/signup")
api.add_resource(LoginResource, "/login")
api.add_resource(Profile, "/profile/<string:user_id>")
api.add_resource(LogoutResource, "/logout")
api.add_resource(RefreshResource, "/refresh_token")
api.add_resource(TagResource, "/tags", "/tags/<string:user_id>")
api.add_resource(Conversation, "/conversation/<string:user_id1>/<string:user_id2>")
