from flask import Flask, render_template, request, redirect
from flask import Blueprint

from budgie.models.transaction import Transaction
from budgie.models.merchant import Merchant
from budgie.models.tag import Tag

import budgie.repositories.transaction_repository as transaction_repository
import budgie.repositories.merchant_repository as merchant_repository
import budgie.repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# show all tags
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)

# show a tag by id
# GET 'tags/<id>'
@tags_blueprint.route("/tags/,<id>")
def show(id):
    tag = tag_repository.select(id)
    tags = tag_repository.select_all()
    return render_template("tags/show.html", tag=tag, tags=tags)


# CREATE - add a new tag
@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    category = request.form['category']
    tag = Tag(category)
    tag_repository.save(tag)
    return redirect('/tags')

# EDIT get - edit a tag
@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    # tags = tag_repository.select_all() what here??
    return render_template("tags/edit.html", tag=tag, tags=tags)