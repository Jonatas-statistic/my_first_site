from flask import redirect, url_for
from flaskr.db import get_db
from flaskr.auth import login_required

from . import bp, get_post


@bp.route('/<int:id>/delete', methods = ("POST",))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))