import flask

from src.api.screeners import crud

blueprint = flask.Blueprint('admin', 'admin')


@blueprint.route('/admin')
def index():
    screeners = crud.get_all_responses()
    return flask.render_template('admin/index.html', screeners=screeners)


# @blueprint.route('/admin/fulfill/<order_id>')
# def fulfill(order_id: int):
#     order = order_service.find_order_by_id(order_id)
#     if not order:
#         return flask.abort(404)
#
#     order_service.fulfill_order(order_id)
#
#     # TODO: Send whatsapp message to notify the customer!
#
#     return flask.redirect('/admin')

