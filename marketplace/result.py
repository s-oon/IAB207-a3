from flask import Blueprint, render_template, request
from .models import Listing
from . import db
from sqlalchemy import desc


bp = Blueprint('result', __name__, url_prefix='/results')

@bp.route('/condition_id=<game_condition>') 
def condition(game_condition):
    listings = Listing.query \
    .filter_by(game_condition=game_condition) \
    .order_by(desc(Listing.date_posted)).all()
    return render_template('result.html', listings=listings)


@bp.route('/classification_id=<game_classification>') 
def classification(game_classification):
    listings = Listing.query \
    .filter_by(game_classification=game_classification) \
    .order_by(desc(Listing.date_posted)).all()
    return render_template('result.html', listings=listings)

@bp.route('/platform_id=<game_platform>') 
def platform(game_platform):
    listings = Listing.query \
    .filter_by(game_platform=game_platform) \
    .order_by(desc(Listing.date_posted)).all()
    return render_template('result.html', listings=listings)

@bp.route('/genre_id=<game_genre>') 
def genre(game_genre):
    listings = Listing.query \
    .filter_by(game_genre=game_genre) \
    .order_by(desc(Listing.date_posted)).all()
    return render_template('result.html', listings=listings)

# @bp.route('/')
# def home():
#     listings = Listing.query.order_by(desc(Listing.date_posted)).limit(8).all()
#     # game1 = Listing(listing_title = "Hello", purchase_price = "$74.00",
#     # game_platform = "XBOX")
#     # game2 = Listing(listing_title = "Hello2", purchase_price = "$74.00",
#     # game_platform = "XBOX")
#     # game3 = Listing(listing_title = "Hello3", purchase_price = "$74.00",
#     # game_platform = "XBOX")
#     # my_list = [game1, game2, game3]
#     flash("Welcome to Australia's newest peer-to-peer marketplace. Register or log-in now to unlock the full potential of Gamerverse!", 'warning')
#     return render_template('Homepage.html', listings = listings)