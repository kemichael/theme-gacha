from flask import Blueprint, request, jsonify
from ..crud import create_theme2, get_theme2s, delete_theme2
from ..schemas import theme2_schema

bp = Blueprint('theme2', __name__, url_prefix='/theme2')

@bp.route('', methods=['GET'])
def list_theme2():
    themes = get_theme2s()
    return jsonify([theme2_schema(t) for t in themes])

@bp.route('', methods=['POST'])

# add_theme2 DB登録
def add_theme2():
    # 複数行対応
    names = request.json.get('names')
    if names:
        name_list = [n.strip() for n in names.split('\n') if n.strip()]
        themes = [theme2_schema(t) for t in create_theme2s(name_list)]
        return jsonify(themes), 201
    else:
        name = request.json.get('name')
        theme = create_theme2(name)
        return jsonify(theme2_schema(theme)), 201

@bp.route('/<int:theme_id>', methods=['DELETE'])

# remove_theme2 物理削除
def remove_theme2(theme_id):
    if delete_theme2(theme_id):
        return jsonify({"result": "ok"})
    return jsonify({"result": "not found"}), 404
