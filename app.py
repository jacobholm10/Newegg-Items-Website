from flask import Flask, render_template, request
from newegg_webscrape import scrape_newegg_products

app = Flask(__name__)


#Newegg products
@app.route('/', methods=['GET','POST'])
def display_newegg_products():
    if request.method == 'POST':
        search_term = request.form['search_term']
        products = scrape_newegg_products(search_term)

        sorted_items = sorted(products.items(), key=lambda x: x[1]['price'])

        return render_template('index.html', sorted_items=sorted_items)
    
    return render_template('index.html', sorted_items=[])
    




if __name__ == '__main__':
    app.run(debug=True)



