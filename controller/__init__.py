from flask import Blueprint

controllerBlueprint = Blueprint("controller", __name__)

from controller import \
    adminController,\
    homeController,\
    authController