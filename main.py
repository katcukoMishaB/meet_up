from app import app, api
from controllers.page_controller import PageConroller
from controllers.user_controller import UserController
from controllers.tags_controller import TagsController
from controllers.match_controller import MatchController
from controllers.skip_controller import SkipController

api.add_resource(PageConroller)
api.add_resource(UserController)
api.add_resource(TagsController)
api.add_resource(MatchController)
api.add_resource(SkipController)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")