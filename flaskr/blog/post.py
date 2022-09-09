from flask import render_template, request

from . import bp, get_post


@bp.route('/<int:id>/post', methods=('GET', 'POST'))
def single_post(id):
    post = get_post(id)

    if request.method == 'POST':
        pass

    return render_template('blog/post.html', post=post)
