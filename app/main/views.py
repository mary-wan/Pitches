from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Upvote,Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
import datetime

@main.route('/')
def index():
    pitches = Pitch.query.all()
    advertisement = Pitch.query.filter_by(category = 'Advertisement').all()
    interview = Pitch.query.filter_by(category = 'Interview').all() 
    product = Pitch.query.filter_by(category = 'Product').all()
    technology = Pitch.query.filter_by(category = 'Technology').all() 
    
    return render_template('index.html', interview = interview,product = product, pitches = pitches,advertisement= advertisement,technology=technology)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        
        new_pitch = Pitch(title = title,post=post,category=category,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
        
    return render_template('new_pitch.html', form = form)

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        new_comment = Comment(comment = comment,pitch_id = pitch_id,user=current_user)
        new_comment.save_comment()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    
    return render_template('comment.html', form =form, pitch = pitch,comments=comments)

@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data  
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))
