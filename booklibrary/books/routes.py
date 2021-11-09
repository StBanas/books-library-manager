import os

from flask import Blueprint
from flask import request, render_template, flash, redirect, url_for
from flask_login import login_required
import booklibrary.books.forms
from booklibrary.books.forms import BookForm, TopForm
from booklibrary import db
import easyocr
import base64
from PIL import Image, ImageOps
from flask_marshmallow import Marshmallow
from booklibrary.models import Book, Top

booky = Blueprint('booky', __name__)
my_books = Blueprint('my_books', __name__)
ma = Marshmallow(booklibrary)

# Book Schema
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'author', 'title')

# Top Schema
class TopSchema(ma.Schema):
    class Meta:
        fields = ('id', 'author1', 'title1')

# Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)

top_schema = TopSchema()
tops_schema = TopSchema(many=True)

# Add Book from image
@booky.route('/book/modify/add/image', methods=['GET', 'POST'])
@login_required
def add_image():
    image_dir = os.path.abspath(os.path.dirname(__file__))
    print("images are here: " + image_dir)
    form = BookForm(request.form)
    data = request.get_json()
    textAreaData = ""
    if (data != None):
        try:
            for key, value in data.items():
                with open("templates/view.png", "wb") as imgFile:
                    data = base64.b64decode(value)
                    imgFile.write(data)

            with open("templates/ocr.txt", "w") as f:
                print("ocr.text ready")
                reader = easyocr.Reader(['pl'])
                textAreaData = reader.readtext(
                    'templates\\view.png', detail=0)
                for i in textAreaData:
                    f.write(i + " ")
                    f.close()
                    return " ".join(textAreaData)
        except:
            AttributeError: print("AttributeError occured - process terminated")
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        return redirect(
            url_for("booky.add_image"))  # TODO - in "getImage.html" to getElementById( id of inside thr image/button )
    return render_template('getImage.html', title="Image", textAreaData=textAreaData, form=form)  # TODO : removed fot check , books=books

# Add Book from Capture
@booky.route('/book/modify/add/capture', methods=['GET', 'POST'])
@login_required
def add_capture():
    form = BookForm(request.form)
    data = request.get_json()
    textAreaData = ""
    if (data != None):
        try:
            for key, value in data.items():
                with open("templates/view.png", "wb") as imgFile:
                    data = base64.b64decode(value)
                    imgFile.write(data)
                    im = Image.open('templates/view.png')
                    im_mirror = ImageOps.mirror(im)
                    im_mirror.save('templates/view.png', quality=95)

            with open("templates/ocr.txt", "w") as f:

                reader = easyocr.Reader(['pl'])
                textAreaData = reader.readtext('templates\\view.png', detail=0)
                for i in textAreaData:
                    f.write(i + " ")
                    f.close()
                    return " ".join(textAreaData)
                print("ocr.text ready")
        except:
            AttributeError: print("AttributeError occured - process terminated")
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("booky.add_capture"))
    return render_template("capture.html", title="Capture", form=form, textAreaData=textAreaData)


# Add Book by JSON ==
@booky.route('/book/modify/add/json', methods=['POST', 'GET'])
@login_required
def modify_add_json():
    author = request.json['author']
    title = request.json['title']
    books = Book(author, title)
    db.session.add(books)
    db.session.commit()
    return book_schema.jsonify(books)


# Create add _manual endpoint
@booky.route('/book/modify/add/mode/manual', methods=['GET', 'POST'])
@login_required
def addManual():
    form = BookForm(request.form)
    books = Book.query.all()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("booky.addManual"))
    return render_template("addManual.html", title="Manual", form=form,books=books)  #


# Create add_text endpoint
@booky.route('/book/modify/add/mode/text', methods=['GET', 'POST'])
@login_required
def add_text():
    form = BookForm(request.form)
    books = Book.query.all()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("booky.add_text"))
    return render_template("getText.html", title="text", form=form, books=books)

# Create update endpoint
@booky.route('/book/modify/mode/update', methods=['GET', 'POST'])
@login_required
def updateBook():
    form = BookForm(request.form)
    books = Book.query.all()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(books)
        db.session.commit()
        flash("Updated Book Successfully")
        return redirect(url_for("booky.updateBook"))
    return render_template("updateJSON.html", title="Update", form=form, books=books)

# Update Book
@booky.route("/book/modify/update/<int:book_id>", methods=["GET", "POST"])
@login_required
def update_book(book_id):
    book = Book.query.get(book_id)
    form = BookForm(request.form, obj=book)
    if form.validate_on_submit():
        form.populate_obj(book)
        db.session.commit()
        flash("Book Updated Successfully")
        return redirect(url_for("booky.updateBook")) #TODO
    return render_template("update.html", title="Update", form=form, book=book)

# Create delete endpoint
@booky.route('/book/modify/mode/delete', methods=['GET', 'POST'])
@login_required
def deleteBook():
    form = BookForm(request.form)
    books = Book.query.all()
    if form.validate_on_submit():
        book = Book(author=form.author.data, title=form.title.data)
        db.session.add(book)
        db.session.commit()
        flash("Book Deleted Successfully")
        return redirect(url_for("booky.deleteBook"))
    return render_template("delete.html", title="Delete", form=form, books=books)

# Create modify endpoint
@booky.route('/book/modify/mode', methods=['GET', 'POST'])
@login_required
def modify_mode():
    return render_template("modify.html", title="Mode")

# Get List of All Books
@booky.route('/book/list', methods=['GET'])
def get_books():
    form = BookForm(request.form)
    books = Book.query.all()
    return render_template("list.html", title="List", form=form, books=books)

# Top 1000
@booky.route('/book/top/list', methods=['GET'])
# @login_required
def top():
    form = TopForm(request.form)
    tops = Top.query.all()
    return render_template('topList.html', title="TopList", form=form, tops=tops)

# Top 1000 add
@booky.route('/book/top/list/add', methods=['GET', 'POST'])
@login_required
def top_add():
    form = TopForm(request.form)
    if form.validate_on_submit():
        top = Top(author1=form.author1.data, title1=form.title1.data)
        db.session.add(top)
        db.session.commit()
        return redirect(url_for("booky.top_add"))
    return render_template('top.html', title="TopAdd", form=form)

# Create delete endpoint
@booky.route('/book/modify/mode/deleteTop', methods=['GET', 'POST'])
@login_required
def deleteTop():
    form = TopForm(request.form)
    tops = Top.query.all()
    if form.validate_on_submit():
        top = Top(author1=form.author.data, title1=form.title.data)
        db.session.add(top)
        db.session.commit()
        flash("Book Deleted Successfully")
        return redirect(url_for("booky.deleteTop"))
    return render_template("deleteTop.html", title="Delete", form=form, tops=tops)

# Create delete Book
@booky.route("/book/modify/delete/<int:book_id>", methods=["GET", "POST"])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return render_template("modify.html", title="Delete")

