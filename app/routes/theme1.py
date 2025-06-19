from flask import Blueprint, request, jsonify
from ..crud import create_theme1, get_theme1s, delete_theme1
from ..schemas import theme1_schema

bp = Blueprint('theme1', __name__, url_prefix='/theme1')

@bp.route('', methods=['GET'])
def list_theme1():
    themes = get_theme1s()
    return jsonify([theme1_schema(t) for t in themes])

@bp.route('', methods=['POST'])

# add_theme1 テーマ追加ロジック
def add_theme1():
    # 複数行対応
    names = request.json.get('names')
    if names:
        name_list = [n.strip() for n in names.split('\n') if n.strip()]
        themes = [theme1_schema(t) for t in create_theme1s(name_list)]
        return jsonify(themes), 201
    else:
        name = request.json.get('name')
        theme = create_theme1(name)
        return jsonify(theme1_schema(theme)), 201

@bp.route('/<int:theme_id>', methods=['DELETE'])

# remove_theme1 物理削除
def remove_theme1(theme_id):
    if delete_theme1(theme_id):
        return jsonify({"result": "ok"})
    return jsonify({"result": "not found"}), 404
