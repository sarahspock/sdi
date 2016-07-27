from flask import Blueprint
import views

mod_front = Blueprint('mod_front', __name__, url_prefix='/form', template_folder='templates',
                          static_folder='', static_url_path='')
