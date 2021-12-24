from app.controllers.goodreads import GoodreadsController
from fastack import Fastack


def init_controllers(app: Fastack):
    app.include_controller(GoodreadsController())
