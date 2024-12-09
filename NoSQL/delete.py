from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId, InvalidId
from config import collection

# Create a Blueprint for the update functionality
delete_bp = Blueprint('delete', __name__)

@delete_bp.route('/delete/<id>', methods=['POST'])

def delete(id):
    try:
        try:
            obj_id = ObjectId(id)
        except InvalidId:
            obj_id = id
        collection.delete_one({"_id": obj_id})
        return redirect(url_for ('index'))
    except Exception as e:
        return str(e), 400