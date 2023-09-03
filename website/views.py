from flask import Blueprint, render_template, request
from webscrape.newegg_webscrape import scrape_newegg_products

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')


#Newegg products
@views.route('/newegg-prices', methods=['GET','POST'])
def display_newegg_products():
    if request.method == 'POST':
        search_term = request.form['search_term']
        products = scrape_newegg_products(search_term)

        sorted_items = sorted(products.items(), key=lambda x: x[1]['price'])

        return render_template('newegg.html', sorted_items=sorted_items)
    
    return render_template('newegg.html', sorted_items=[])