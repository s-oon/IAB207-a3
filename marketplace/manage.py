from flask import Blueprint, render_template, abort
from flask_login import login_required
from .models import Listing, Bid, User, Transaction
from . import db

bp = Blueprint('manage', __name__, url_prefix='/manage')


@bp.route('/<id>')
@login_required
def manage(id):
    listing = Listing.query.filter_by(id=id).first_or_404()
    bids = Bid.query.filter_by(listing_id=id).join(User, Bid.user_id==User.id).\
    add_columns(User.user_name, Bid.contact_number, Bid.date_of_bid).all()
    users = User.query.all()
    return render_template('ManageListing.html', listing=listing, bids=bids, user=users)
