from flask import Blueprint, jsonify
from ..models import Team, Theme1, Theme2
from ..database import db
import random

bp = Blueprint('draw', __name__, url_prefix='/draw')

@bp.route('', methods=['POST'])
def draw():
    teams = Team.query.all()
    theme1s = Theme1.query.all()
    theme2s = Theme2.query.all()
    if not teams or not theme1s or not theme2s:
        return jsonify({"error": "データが足りないよ！"}), 400

    if len(teams) > len(theme1s) or len(teams) > len(theme2s):
        return jsonify({"error": "テーマ数がチーム数より少ないからダブりなし抽選できないよ！"}), 400

    # ダブりなしでランダムにテーマを割り当て
    shuffled_theme1s = random.sample(theme1s, len(teams))
    shuffled_theme2s = random.sample(theme2s, len(teams))

    results = []
    for i, team in enumerate(teams):
        t1 = shuffled_theme1s[i]
        t2 = shuffled_theme2s[i]
        results.append({
            "team": team.name,
            "theme1": t1.name,
            "theme2": t2.name
        })
    return jsonify(results)