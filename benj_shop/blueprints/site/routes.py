from flask import Blueprint, flash, redirect, render_template, request

#internal import
from benj_shop.models import Product, db
from benj_shop.forms import ProductForm

#need to instantiate our Blueprint class

site = Blueprint('site', __name__, template_folder='site_templates')

#use site object to create our routes
@site.route('/')
def shop():

    #query our database > grab products to disply
    allprods = Product.query.all() #the same as SELECT * FROM products

                    #in render_template: left sdie html, right side our route
    return render_template('shop.html', shop=allprods)

@site.route('/shop/create', methods= ['GET', 'POST'])
def create():

    #instantiate our productionform

    createform = ProductForm()

    if request.method == 'POST' and createform.validate_on_submit():
        #grab our data from our form
        name = createform.name.data
        image = createform.image.data
        description = createform.description.data
        make = createform.make.data
        model = createform.model.data
        year = createform.year.data
        milage = createform.milage.data
        price = createform.price.data
        quantity = createform.quantity.data

        #instantiate that class as an object passing in our arguments to replace our parameters
        product = Product(name, image, description, make, model, year, milage, price, quantity )

        db.session.add(product)
        db.session.commit()

        flash(f"You have succesfully created product {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We can't process your request", category='warning')
        return redirect('/shop/create')
    
    return render_template('create.html', form=createform )

@site.route('/shop/update/<id>', methods=['GET', 'POST']) #<PARAMETER> this is how pass parameters to our routes
def update(id):

    #lets grab our specific product we want to update
    product = Product.query.get(id) #this should only ever bring back 1 item/object
    updateform = ProductForm()

    if request.method == 'POST' and updateform.validate_on_submit():

        product.name = updateform.name.data
        product.image = updateform.image.data
        product.description = updateform.description.data
        product.make = updateform.make.data
        product.model = updateform.model.data
        product.year = updateform.year.data
        product.milage = updateform.milage.data
        product.price = updateform.price.data
        product.quantity = updateform.quantity.data

        db.session.commit()

        flash(f"You have successfully updated product {product.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/')
    
    return render_template('update.html', form=updateform, product=product )

@site.route('/shop/delete/<id>')
def delete(id):

    #query our database to find that object we want to delete
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/')