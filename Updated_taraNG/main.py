from flask import Flask, render_template, request, escape, redirect, url_for, session, flash
from passlib.hash import sha256_crypt
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
#import flask_whooshalchemy as wa
import os
from random import randint
import zipfile
import json


app = Flask(__name__)
app.secret_key = "myTaraNG_is_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@127.0.0.1:3306/my_tarang"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['WHOOSH_BASE'] = 'whoosh'

db = SQLAlchemy(app)
db.create_all()

class Admin(db.Model):
    __tablename__= 'admin'
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(64), index=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    remember_token = db.Column(db.String(128), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, email, password, phone, remember_token=None):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def __repr__(self):
        return '<Admin %r>' % self.email


class Students(db.Model):
    __tablename__= 'students'
    #__searchable__= ['name']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    institute = db.Column(db.String(128), nullable=False)

    phone = db.Column(db.String(15), nullable=True)
    photo = db.Column(db.String(128), nullable=True)
    year = db.Column(db.String(40), nullable=True)

    internship = db.Column(db.String(1024), nullable=True)
    skills = db.Column(db.String(255), nullable=True)
    department = db.Column(db.String(128), nullable=True)
    achievements = db.Column(db.String(1024), nullable=True)
    projects = db.Column(db.String(1024), nullable=True)
    publications = db.Column(db.String(1024), nullable=True)

    teachers = db.Column(db.String(128), nullable=True)
    email_verified = db.Column(db.SmallInteger(), default=0)
    admin_verified = db.Column(db.SmallInteger(), default=0)
    google_provider_id = db.Column(db.String(128), nullable=True)
    facebook_provider_id = db.Column(db.String(128), nullable=True)
    batch_ids = db.Column(db.String(128), nullable=True)
    remember_token = db.Column(db.String(128), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)
    followed_assignments = db.Column(db.String(1024), nullable=True)

    def __init__(self, name, email, password, institute, year=None, google_provider_id=None,
     facebook_provider_id=None, batch_ids=None, remember_token=None):
        self.name = name
        self.email = email
        self.password = password
        self.institute = institute
        #phone = 0
        if year: self.year=year
        if(google_provider_id): self.google_provider_id = google_provider_id
        if(facebook_provider_id): self.facebook_provider_id = facebook_provider_id
        if(batch_ids): self.batch_ids = batch_ids
        if(remember_token): self.remember_token = remember_token

    def __repr__(self):
        return '<Students %r>' % self.email


class Lecturers(db.Model):
    __tablename__= 'lecturers'
    #__searchable__= ['name']
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    institute = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    photo = db.Column(db.String(128), nullable=True)
    designation = db.Column(db.String(128), nullable=True)
    education = db.Column(db.String(128), nullable=True)
    skills = db.Column(db.String(255), nullable=True)
    about = db.Column(db.String(1024), nullable=True)
    experience = db.Column(db.String(1024), nullable=True)
    achievements = db.Column(db.String(1024), nullable=True)
    students_request = db.Column(db.String(1024), nullable=True)
    lecturers_request = db.Column(db.String(1024), nullable=True)
    teachers = db.Column(db.String(1024), nullable=True)
    linkedin = db.Column(db.String(255), nullable=True)
    github = db.Column(db.String(255), nullable=True)
    youtube = db.Column(db.String(255), nullable=True)
    email_verified = db.Column(db.SmallInteger(), default=0)
    google_provider_id = db.Column(db.String(128), nullable=True)
    facebook_provider_id = db.Column(db.String(128), nullable=True)
    batch_ids = db.Column(db.String(128), nullable=True)
    remember_token = db.Column(db.String(128), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)
    students_accepted = db.Column(db.String(1024), nullable=True)
    lecturers_accepted = db.Column(db.String(1024), nullable=True)
    created_assignments = db.Column(db.String(1024), nullable=True)
    followed_assignments = db.Column(db.String(1024), nullable=True)
    subjects = db.Column(db.String(1024), nullable=True)
    membership = db.Column(db.String(128), nullable=True)
    department = db.Column(db.String(128), nullable=True)
    projects = db.Column(db.String(1024), nullable=True)
    publications = db.Column(db.String(1024), nullable=True)


    def __init__(self, name, email, password, institute, google_provider_id=None, facebook_provider_id=None):
        self.name = name
        self.email = email
        self.password = password
        self.institute = institute
        if(google_provider_id): self.google_provider_id = google_provider_id
        if(facebook_provider_id): self.facebook_provider_id = facebook_provider_id

    def __repr__(self):
        return '<Lecturers %r>' % self.email



class Assignments(db.Model):
    __tablename__= 'assignments'
    #__searchable__= ['topic_name']
    id = db.Column(db.Integer, primary_key=True)
    lecturer_id = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    topic_name = db.Column(db.String(255), index=False, nullable=False)
    path = db.Column(db.String(128), nullable=False)
    topic_type = db.Column(db.String(128), nullable=True)
    topic_abstract = db.Column(db.String(1024), nullable=True)
    topic_subject = db.Column(db.String(128), nullable=True)
    topic_chapter = db.Column(db.String(128), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now)
    upvotes = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String(1024), nullable=True)
    resource_center = db.Column(db.String(128), nullable=False)

    def __init__(self, lecturer_id, author_id, topic_name, path, topic_type, topic_abstract, topic_subject, topic_chapter):
        self.lecturer_id = lecturer_id
        self.author_id = author_id
        self.topic_name = topic_name
        self.path = path
        self.topic_type = topic_type
        self.topic_abstract = topic_abstract
        self.topic_subject = topic_subject
        self.topic_chapter = topic_chapter
        self.upvotes = 0
        self.resource_center = 'False'
        #self.topic_contrib = topic_contrib

    def __repr__(self):
        return '<Assignments %r>' % self.path

#wa.whoosh_index(app, Lecturers)


def create_user(req):
    #try:
        name = str(req.form['name'])
        email = str(req.form['email'])
        password = str(req.form['password']) #sha256_crypt.hash(
        institute = str(req.form['institute'])
        if  request.form['user_type'] == 'student':
            student = Students(name,email,password,institute)
            db.session.add(student)
            db.session.commit()
            return True
        if  request.form['user_type'] == 'teacher':
            lecturer = Lecturers(name,email,password,institute)
            db.session.add(lecturer)
            db.session.commit()
            return True
    #except Exception:
    #    return False

@app.route('/signup')
def signup():
    return render_template('signup.html', the_title='Sign Up - myTaraNG')


@app.route('/signup_success', methods = ['POST', 'GET'])
def signup_success():
    if request.method == 'POST':
        boolean = create_user(request)
        if boolean == True:
            flash('Successfully sign up, you can login now')
            return redirect('/login')
        else:
            flash('Error occurred ! Please try again')
            return redirect('/signup')

def login_credential_check(req):
    try:
        username = str(req.form['username'])
        password = str(req.form['password'])
        student = Students.query.filter_by(email=username).first()
        if student.email == username and password == student.password: #sha256_crypt.verify(
            session['username'] = student.email
            session['user_id'] = student.id
            session['user_type'] = 'student'
            return True
        else:
            return False
    except Exception:
        return False
def lecturer_login_credential_check(req):
    try:
        username = str(req.form['username'])
        password = str(req.form['password'])
        lecturer = Lecturers.query.filter_by(email=username).first()
        if lecturer.email == username and password==lecturer.password: #sha256_crypt.verify(password, lecturer.password)
            session['username'] = lecturer.email
            session['user_id'] = lecturer.id
            session['user_type'] = 'teacher'
            return True
        else:
            return False
    except Exception:
        return False


@app.route('/')
@app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html', the_title='Login - myTaraNG')


@app.route('/login_success', methods = ['POST', 'GET'])
def login_success():
    if request.method == 'POST':
        if  request.form['user_type'] == 'student':
            credential = login_credential_check(request)
        if  request.form['user_type'] == 'teacher':
            credential = lecturer_login_credential_check(request)
        if credential != False:
            return redirect(url_for('dashboard'))
        else:
            flash('Login credentials do not match')
            return redirect('/login')
        return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('username', None);
    session.pop('user_id', None);
    session.pop('user_type', None);
    return redirect('login')


@app.route('/ForgotPassword')
def ForgotPassword():
    return render_template('ForgotPassword.html',
                           the_title='Forgot Password - myTaraNG')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    elif session['user_type']=='student':
        student = Students.query.filter_by(email=session['username']).first()
        assignments_all = Assignments.query.all()
        teachers = []; assignments_followed = [];
        if student.teachers != None:
            teachers = [Lecturers.query.filter_by(id=int(i)).first() for i in student.teachers.split(',')]
        if student.followed_assignments != None:
            assignments_followed = [Assignments.query.filter_by(id=int(i)).first() for i in student.followed_assignments.split(',')];

        return render_template('dashboard/dashboard_student.html',
                           the_title= 'Dashboard - myTaraNG',
                           student= student,
                           teachers= teachers,
                           assignments_all= assignments_all,
                           assignments_followed= assignments_followed)

    elif session['user_type']=='teacher':
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        assignments_own = Assignments.query.filter_by(lecturer_id=lecturer.id).all()
        assignments_all = Assignments.query.all()
        teachers = []; votes = 0; num_students = 0;

        if lecturer.teachers != None:
            teachers = [Lecturers.query.filter_by(id=int(i)).first() for i in lecturer.teachers.split(',')]
        assignments_followed = [];
        if lecturer.followed_assignments != None:
            assignments_followed = [Assignments.query.filter_by(id=int(i)).first() for i in lecturer.followed_assignments.split(',')];
            #for assignment_id in lecturer.followed_assignments: assignments_followed.append(Assignments.query.filter_by(id=assignment_id).first())

        if assignments_own != None:
            for ass_votes in assignments_own: votes += ass_votes.upvotes
        #if lecturer.lecturers_accepted != None: num_students += len(lecturer.lecturers_accepted)
        if lecturer.students_accepted != None: num_students += len(lecturer.students_accepted.split(','))
        return render_template('dashboard/dashboard_lecturer.html',
                           the_title='Lecturer Dashboard - myTaraNG',
                           lecturer= lecturer,
                           teachers= teachers,
                           assignments_own=assignments_own,
                           assignments_all=assignments_all,
                           upvotes= votes,
                           num_students = num_students,
                           assignments_followed= assignments_followed)

@app.route('/edit_dashboard')
def edit_dashboard():
    if 'username' not in session:
        return redirect('/login')
    else:
        if session['user_type']=='student':
            user = Students.query.filter_by(email=session['username']).first()
        elif session['user_type']=='teacher':
            user = Lecturers.query.filter_by(email=session['username']).first()
        return render_template('dashboard/lecturer_edit_dashboard.html',
                           the_title='Edit Profile - myTaraNG',
                           lecturer=user, user_type=session['user_type'])


@app.route('/edit_dashboard_success', methods = ['GET','POST'])
def edit_dashboard_success():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'POST':
        #try:
            if session['user_type']=='student':
                user = Students.query.filter_by(email=session['username']).first()
            elif session['user_type']=='teacher':
                user = Lecturers.query.filter_by(email=session['username']).first()
            user.name = request.form['name']
            user.phone = request.form['phone']
            user.institute = request.form['institute']
            #
            if session['user_type']=='teacher':
                if request.form['membership'] != None:
                    user.designation = request.form['designation']
                if request.form['membership'] != None: #
                    user.membership = request.form['membership']
                if request.form['subjects'] != None:
                    user.subjects = request.form['subjects']#
                if request.form['experience'] != None:
                    user.experience = request.form['experience']#
                if request.form['education'] != None:
                    user.education = request.form['education']#
            if session['user_type']=='student':
                if request.form['internship'] != None:
                    user.internship = request.form['internship']#
                if request.form['year'] != None:
                    user.year = request.form['year']#

            if request.form['department'] != None:
                user.department = request.form['department']
            if request.form['skills'] != None:
                user.skills = request.form['skills']
            if request.form['about'] != None:
                user.about = request.form['about']
            if request.form['achievements'] != None:
                user.achievements = request.form['achievements']
            if request.form['projects'] != None:
                user.projects = request.form['projects']
            if request.form['publications'] != None:
                user.publications = request.form['publications']

            #if request.form['linkedin'] != None:
            #    lecturer.linkedin = request.form['linkedin']
            #if request.form['github'] != None:
            #    lecturer.github = request.form['github']
            #if request.form['youtube'] != None:
            #    lecturer.youtube = request.form['youtube']

            if session['user_type']=='teacher': image_dir = "./static/img/lecturers"
            if session['user_type']=='student': image_dir = "./static/img/students"
            image_file = request.files['photo']
            file_name = secure_filename(image_file.filename)
            fileext = file_name.split('.')
            if len(fileext)>1:
                file_name_new = image_dir +'/' + str(user.id)+'.'+fileext[1]
                image_file.save(file_name_new)
                if session['user_type']=='teacher': user.photo = 'img/lecturers/'+ str(user.id)+'.'+fileext[1];
                if session['user_type']=='student': user.photo = 'img/students/'+ str(user.id)+'.'+fileext[1];

            db.session.commit()
            return redirect('/dashboard')
        #except Exception:
        #   raise redirect('/dashboard')


####################################### Search Profile #######################################

@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'username' not in session: #student_username
        return redirect('/login')
    else:
        print(request.args.get('query'))
        lecturers = Lecturers.query.all() #whoosh_search('Lecturer')#request.args.get('query')
        #print(Lecturers.query.whoosh_search('Lecturer Name'))#whoosh_search('Name').

        #student = Students.query.filter_by(email=session['student_username']).first()
        #notes = Assignments.query.all()
        #request_accepted = [int(i) for i in student.teachers.split(',')]
        return render_template('dashboard/search.html',
                           the_title='Search - myTaraNG',
                           lecturers=lecturers)


@app.route('/profile/<id>')
def profile(id):
    lecturer_to_follow = Lecturers.query.filter_by(id=id).first()
    assignments = Assignments.query.filter_by(lecturer_id=lecturer_to_follow.id).all()
    if 'username' not in session: #student_username
        return redirect('/login')
    else:
        if int(session['user_id'])==int(id) and session['user_type'] == 'teacher':
            return redirect('/dashboard')
        else:
            request_accepted_bool = False; request_send_bool = False;
            if session['user_type'] == 'teacher':
                lecturer = Lecturers.query.filter_by(email=session['username']).first()
                if lecturer_to_follow.lecturers_accepted != None:
                    request_accepted = [int(i) for i in lecturer_to_follow.lecturers_accepted.split(',')]
                    request_accepted_bool = lecturer.id in request_accepted
                if lecturer_to_follow.lecturers_request != None:
                    lecturers_request = [int(i) for i in lecturer_to_follow.lecturers_request.split(',')]
                    request_send_bool = lecturer.id in lecturers_request
            if session['user_type'] == 'student':
                student = Students.query.filter_by(email=session['username']).first()
                print('student_name_:',student)
                if lecturer_to_follow.students_accepted != None:
                    request_accepted = [int(i) for i in lecturer_to_follow.students_accepted.split(',')]
                    print('request_accepted_:',request_accepted)
                    request_accepted_bool = student.id in request_accepted
                if lecturer_to_follow.students_request != None:
                    students_request = [int(i) for i in lecturer_to_follow.students_request.split(',')]
                    request_send_bool = student.id in students_request
            return render_template('dashboard/profile.html',
                           the_title='Profile - myTaraNG',
                           id=int(id),
                           request_accepted_bool = request_accepted_bool,
                           request_send_bool = request_send_bool, #pending
                           assignments=assignments,
                           lecturer_to_be_visited=lecturer_to_follow,
                           user_type = session['user_type'])

@app.route('/profile_student/<id>')
def profile_student(id):
    student_to_be_visited = Students.query.filter_by(id=id).first()
    if 'username' not in session: #student_username
        return redirect('/login')
    else:
        if int(session['user_id'])==int(id) and session['user_type'] == 'student':
            return redirect('/dashboard')
        else:
            return render_template('dashboard/profile_student.html',
                           the_title='Profile - myTaraNG',
                           id=int(id),
                           student_to_be_visited=student_to_be_visited,
                           user_type = session['user_type'])


##################################### Assignment section ##########################################
@app.route('/lecturer')

@app.route('/lecturer/create_assignment')
def lecturer_create_assignment():
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        return render_template('dashboard/create_assignment.html',
                           the_title='Create Assignments - myTaraNG',
                           lecturer=lecturer)


@app.route('/lecturer/create_assignment_success', methods = ['POST', 'GET'])
def lecturer_create_assignment_success():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'POST':
        try:
            lecturer = Lecturers.query.filter_by(email=session['username']).first()
            directory = str(randint(1000000000, 9999999999))
            parent_dir = "./static/uploads"
            path = os.path.join(parent_dir, directory)
            os.mkdir(path, 0o777)
            #app.config['UPLOAD_FOLDER'] = path
            file = request.files['zip_file']
            file_name = secure_filename(file.filename)
            filename = os.path.join(path, file_name)
            file.save(filename)
            with zipfile.ZipFile(filename, 'r') as zip_ref: zip_ref.extractall(path)
            description_file = os.path.join(path, "description.txt");# print(description_file)
            os.remove(filename)
            with open(description_file, 'r') as f:
                description = json.load(f)
                topic_name = description['contents']['title'];
                topic_type = description['contents']['type'];
                topic_abstract = description['contents']['abstract'];
                topic_subject = description['contents']['subject'];
                topic_chapter = description['contents']['chapter'];
                #topic_contributors= description['contents']['contributors'];
                #print(topic_contributors)
                #lecturer_id = request.form['lecturer_id']
                #topic_name = str(request.form['topic_name'])
                path1 = "uploads/" + directory # + "/" + file_name.split('.')[0]
                assignment = Assignments(lecturer.id,lecturer.id,topic_name,path1, topic_type, topic_abstract, topic_subject, topic_chapter)
                db.session.add(assignment)
                db.session.commit()
                # it should go to my created_assignments
                #lecturer = Lecturers.query.filter_by(id=lecturer_id).first()

                if not lecturer.created_assignments == None:
                    created_assignments = [int(i) for i in lecturer.created_assignments.split(',')]
                    created_assignments.append(assignment.id)
                    created_assignments_str = ','.join(str(i) for i in created_assignments)
                    lecturer.created_assignments = created_assignments_str
                    db.session.commit()
                else:
                    lecturer.created_assignments = str((assignment.id))
                    db.session.commit()

                # it should also go to students/lecturer database followe_assignments
                if lecturer.lecturers_accepted:
                    for i in lecturer.lecturers_accepted.split(','):
                        lecturer_following = Lecturers.query.filter_by(id=int(i)).first()
                        if lecturer_following.followed_assignments:
                            followed_assignments = [int(i) for i in lecturer_following.followed_assignments.split(',')]
                            followed_assignments.append(assignment.id)
                            followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                            lecturer_following.followed_assignments = followed_assignments_str
                            db.session.commit()
                        else:
                            lecturer_following.followed_assignments = str((assignment.id))
                            db.session.commit()
                if lecturer.students_accepted:
                    for i in lecturer.students_accepted.split(','):
                        student_following = Students.query.filter_by(id=int(i)).first()
                        if student_following.followed_assignments:
                            followed_assignments = [int(i) for i in student_following.followed_assignments.split(',')]
                            followed_assignments.append(assignment.id)
                            followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                            student_following.followed_assignments = followed_assignments_str
                            db.session.commit()
                        else:
                            student_following.followed_assignments = str((assignment.id))
                            db.session.commit()


                flash('Successfully created a assignment')
                return redirect('/dashboard')
        except Exception:
            flash('Error occurred ! Please try again')
            return redirect('/lecturer/create_assignment')
    else:
        flash('Error occurred ! Please try again')
        return redirect('/lecturer/create_assignment')

@app.route('/lecturer/adopt_assignment/<id>')
def lecturer_adopt_assignment(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        assignment_new = Assignments(lecturer.id,assignment.author_id,assignment.topic_name,assignment.path, assignment.topic_type, assignment.topic_abstract, assignment.topic_subject, assignment.topic_chapter)
        db.session.add(assignment_new)
        db.session.commit()

        if not lecturer.created_assignments == None:
            created_assignments = [int(i) for i in lecturer.created_assignments.split(',')]
            created_assignments.append(assignment_new.id)
            created_assignments_str = ','.join(str(i) for i in created_assignments)
            lecturer.created_assignments = created_assignments_str
            db.session.commit()
        else:
            lecturer.created_assignments = str((assignment_new.id))
            db.session.commit()

        # it should also go to students/lecturer database followe_assignments
        if lecturer.lecturers_accepted:
            for i in lecturer.lecturers_accepted.split(','):
                lecturer_following = Lecturers.query.filter_by(id=int(i)).first()
                if lecturer_following.followed_assignments:
                    followed_assignments = [int(i) for i in lecturer_following.followed_assignments.split(',')]
                    followed_assignments.append(assignment_new.id)
                    followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                    lecturer_following.followed_assignments = followed_assignments_str
                    db.session.commit()
                else:
                    lecturer_following.followed_assignments = str((assignment_new.id))
                    db.session.commit()
        if lecturer.students_accepted:
            for i in lecturer.students_accepted.split(','):
                student_following = Students.query.filter_by(id=int(i)).first()
                if student_following.followed_assignments:
                    followed_assignments = [int(i) for i in student_following.followed_assignments.split(',')]
                    followed_assignments.append(assignment_new.id)
                    followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                    student_following.followed_assignments = followed_assignments_str
                    db.session.commit()
                else:
                    student_following.followed_assignments = str((assignment_new.id))
                    db.session.commit()

        return redirect('/dashboard')

@app.route('/lecturer/edit_assignment/<id>')
def lecturer_edit_assignment(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        return render_template('dashboard/edit_assignment.html',
                           the_title='Create Assignments - myTaraNG',
                           assignment=assignment)



@app.route('/lecturer/edit_assignment_success', methods = ['POST', 'GET'])
def lecturer_edit_assignment_success():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'POST':
        try:
            update_assignment = Assignments.query.filter_by(id=request.form['assignment_id']).first()
            update_assignment.topic_name = request.form['topic_name']
            update_assignment.topic_abstract = request.form['topic_abstract']
            db.session.commit()
            return redirect('/dashboard')
        except Exception:
            return redirect('/dashboard')


@app.route('/lecturer/delete_assignment/<id>')
def lecturer_delete_assignment(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        try:
            assignment = Assignments.query.filter_by(id=id).first()
            db.session.delete(assignment)
            db.session.commit()
            parent_dir = "./static"
            path = os.path.join(parent_dir, assignment.path)
            os.remove(path)#os.mkdir(path, 0o777)
            return redirect('/dashboard')
        except Exception:
            return redirect('/dashboard')


@app.route('/lecturer/create_annoncement_success', methods = ['POST', 'GET'])
def lecturer_create_announcement_success():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'POST':
        try:
            lecturer = Lecturers.query.filter_by(email=session['username']).first()
            topic_name = request.form['topic_name']
            topic_abstract = request.form['topic_abstract']
            topic_type = "annoncement"
            assignment = Assignments(lecturer.id,lecturer.id,topic_name,'', topic_type, topic_abstract, '', '')
            db.session.add(assignment)
            db.session.commit()
            # it should go to my created_assignments
            #lecturer = Lecturers.query.filter_by(id=lecturer_id).first()

            if not lecturer.created_assignments == None:
                created_assignments = [int(i) for i in lecturer.created_assignments.split(',')]
                created_assignments.append(assignment.id)
                created_assignments_str = ','.join(str(i) for i in created_assignments)
                lecturer.created_assignments = created_assignments_str
                db.session.commit()
            else:
                lecturer.created_assignments = str((assignment.id))
                db.session.commit()

            # it should also go to students/lecturer database followe_assignments
            if lecturer.lecturers_accepted:
                for i in lecturer.lecturers_accepted.split(','):
                    lecturer_following = Lecturers.query.filter_by(id=int(i)).first()
                    if lecturer_following.followed_assignments:
                        followed_assignments = [int(i) for i in lecturer_following.followed_assignments.split(',')]
                        followed_assignments.append(assignment.id)
                        followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                        lecturer_following.followed_assignments = followed_assignments_str
                        db.session.commit()
                    else:
                        lecturer_following.followed_assignments = str((assignment.id))
                        db.session.commit()
            if lecturer.students_accepted:
                for i in lecturer.students_accepted.split(','):
                    student_following = Students.query.filter_by(id=int(i)).first()
                    if student_following.followed_assignments:
                        followed_assignments = [int(i) for i in student_following.followed_assignments.split(',')]
                        followed_assignments.append(assignment.id)
                        followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                        student_following.followed_assignments = followed_assignments_str
                        db.session.commit()
                    else:
                        student_following.followed_assignments = str((assignment.id))
                        db.session.commit()


            flash('Successfully created a announcement')
            return redirect('/dashboard')
        except Exception:
            flash('Error occurred ! Please try again')
            return redirect('/lecturer/create_assignment')
    else:
        flash('Error occurred ! Please try again')
        return redirect('/lecturer/create_assignment')

@app.route('/lecturer/create_embedd_success', methods = ['POST', 'GET'])
def lecturer_create_embedd_success():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'POST':
        try:
            lecturer = Lecturers.query.filter_by(email=session['username']).first()
            topic_name = request.form['topic_name']
            topic_abstract = request.form['topic_abstract']
            topic_type = "embbed_webinar"
            assignment = Assignments(lecturer.id,lecturer.id,topic_name,'', topic_type, topic_abstract, '', '')
            db.session.add(assignment)
            db.session.commit()
            # it should go to my created_assignments
            #lecturer = Lecturers.query.filter_by(id=lecturer_id).first()

            if not lecturer.created_assignments == None:
                created_assignments = [int(i) for i in lecturer.created_assignments.split(',')]
                created_assignments.append(assignment.id)
                created_assignments_str = ','.join(str(i) for i in created_assignments)
                lecturer.created_assignments = created_assignments_str
                db.session.commit()
            else:
                lecturer.created_assignments = str((assignment.id))
                db.session.commit()

            # it should also go to students/lecturer database followe_assignments
            if lecturer.lecturers_accepted:
                for i in lecturer.lecturers_accepted.split(','):
                    lecturer_following = Lecturers.query.filter_by(id=int(i)).first()
                    if lecturer_following.followed_assignments:
                        followed_assignments = [int(i) for i in lecturer_following.followed_assignments.split(',')]
                        followed_assignments.append(assignment.id)
                        followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                        lecturer_following.followed_assignments = followed_assignments_str
                        db.session.commit()
                    else:
                        lecturer_following.followed_assignments = str((assignment.id))
                        db.session.commit()
            if lecturer.students_accepted:
                for i in lecturer.students_accepted.split(','):
                    student_following = Students.query.filter_by(id=int(i)).first()
                    if student_following.followed_assignments:
                        followed_assignments = [int(i) for i in student_following.followed_assignments.split(',')]
                        followed_assignments.append(assignment.id)
                        followed_assignments_str = ','.join(str(i) for i in followed_assignments)
                        student_following.followed_assignments = followed_assignments_str
                        db.session.commit()
                    else:
                        student_following.followed_assignments = str((assignment.id))
                        db.session.commit()


            flash('Successfully created a announcement')
            return redirect('/dashboard')
        except Exception:
            flash('Error occurred ! Please try again')
            return redirect('/lecturer/create_assignment')
    else:
        flash('Error occurred ! Please try again')
        return redirect('/lecturer/create_assignment')

@app.route('/note/<id>')
def note(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        lecturer_assignment= Lecturers.query.filter_by(id=assignment.lecturer_id).first()
        author = Lecturers.query.filter_by(id=assignment.author_id).first()
        submission_status = 'NA'; mark = '0';
        if  session['user_type'] == 'teacher':
            if int(lecturer_assignment.id) == int(session['user_id']): submission_status = 'Owner';
        elif  session['user_type'] == 'student':
            submission_status = 'False';
            if assignment.result != None:
                result = [i for i in assignment.result.split(',')]
                students_ids = result[0::2]; marks = result[1::2];
                students_ids = [int(i) for i in students_ids]
                if int(session['user_id']) in students_ids:
                    submission_status = 'True'; mark = str(marks[students_ids.index(int(session['user_id']))])

        return render_template('dashboard/note.html',
                           the_title='Note - myTaraNG',
                           id=int(id),
                           assignment=assignment,
                           lecturer=lecturer_assignment,
                           author=author,
                           user_type = session['user_type'],
                           submission_status = submission_status,
                           mark=mark)

# @app.route('/note_upvote/<id>')
# def note_upvote(id):
#     if 'username' not in session: #student_username
#         return redirect('/login')
#     else:
#         assignment = Assignments.query.filter_by(id=id).first()
#         assignment.upvotes+=1;
#         db.session.commit()
#         return redirect(url_for('note',id=id))
@app.route('/note_upvote/<id>')
def note_upvote(id):
    if 'username' not in session: #student_username
        return redirect('/login')
        if Assignments.query.filter_by(id=id).exists():
            flash('Duplicate Voting')
        # return redirect(url_for('note',id=id))
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        assignment.upvotes+=1;
        db.session.commit()
        return redirect(url_for('note',id=id))

@app.route('/note_submit_plus/<id>')
def note_submit_plus(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        mark = 'Satisfactory'; result = [];
        if  session['user_type'] == 'student':
            if assignment.result != None:
                result = [i for i in assignment.result.split(',')]
            result.append(str(session['user_id'])); result.append(mark);
            assignment.result = ','.join(str(i) for i in result)
            db.session.commit()
        return redirect(url_for('note',id=id))

@app.route('/note_submit_minus/<id>')
def note_submit_minus(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        mark = 'Not satisfactory'; result = [];
        if  session['user_type'] == 'student':
            if assignment.result != None:
                result = [i for i in assignment.result.split(',')]
            result.append(str(session['user_id'])); result.append(mark);
            assignment.result = ','.join(str(i) for i in result)
            db.session.commit()
        return redirect(url_for('note',id=id))

@app.route('/report/<id>')
def report(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        assignment = Assignments.query.filter_by(id=id).first()
        if  session['user_type'] == 'teacher':
            if int(assignment.lecturer_id) == int(session['user_id']):
                report_table = [];
                if assignment.result != None:
                    result = [i for i in assignment.result.split(',')]
                    students_ids = result[0::2];
                    students_ids = [int(i) for i in students_ids]
                    marks = result[1::2];
                    report_table = [{'Name':Students.query.filter_by(id=int(students_ids[i])).first().name, 'Performance':str(marks[i])} for i in range(len(students_ids))]
                return render_template('dashboard/result_table.html',
                                   the_title='Report - myTaraNG',
                                   assignment=assignment,
                                   report_table=report_table)


##################################### Manage requests ##########################################

@app.route('/send_request/<id>')
def send_request(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer_to_follow = Lecturers.query.filter_by(id=id).first()
        if session['user_type'] == 'teacher':
            if lecturer_to_follow.lecturers_request != None:
                lecturers_request = [int(i) for i in lecturer_to_follow.lecturers_request.split(',')]
                lecturers_request.append(session['user_id'])
                lecturers_request = ','.join(str(i) for i in lecturers_request)
                lecturer_to_follow.lecturers_request = lecturers_request
                db.session.commit()
            else:
                lecturer_to_follow.lecturers_request = str(session['user_id'])
                db.session.commit()
        if session['user_type'] == 'student':
            if lecturer_to_follow.students_request != None:
                students_request = [int(i) for i in lecturer_to_follow.students_request.split(',')]
                students_request.append(session['user_id'])
                students_request = ','.join(str(i) for i in students_request)
                lecturer_to_follow.students_request = students_request
                db.session.commit()
            else:
                lecturer_to_follow.students_request = str(session['user_id'])
                db.session.commit()
        return redirect(url_for('profile',id=id))

@app.route('/cancel_request/<id>')
def cancel_request(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer_to_follow = Lecturers.query.filter_by(id=id).first()
        if session['user_type'] == 'teacher':
            lecturers_request = [int(i) for i in lecturer_to_follow.lecturers_request.split(',')]
            lecturers_request.remove(session['user_id'])
            if lecturers_request != []:
                lecturers_request = ','.join(str(i) for i in lecturers_request)
                lecturer_to_follow.lecturers_request = lecturers_request
                db.session.commit()
            else:
                lecturer_to_follow.lecturers_request = None
                db.session.commit()
            return redirect(url_for('profile',id=id))

        if session['user_type'] == 'student':
            students_request = [int(i) for i in lecturer_to_follow.students_request.split(',')]
            students_request.remove(session['user_id'])
            if students_request != []:
                students_request = ','.join(str(i) for i in students_request)
                lecturer_to_follow.students_request = students_request
                db.session.commit()
            else:
                lecturer_to_follow.students_request = None
                db.session.commit()
            return redirect(url_for('profile',id=id))




@app.route('/lecturer/requests')
def lecturer_requests():
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        lecturers = Lecturers.query.all()
        students = Students.query.all()
        students_request = []; lecturers_request = [];
        if lecturer.students_request != None:
            for i in lecturer.students_request.split(','):
                students_request.append(Students.query.filter_by(id=int(i)).first())
        if lecturer.lecturers_request != None:
            for i in lecturer.lecturers_request.split(','):
                lecturers_request.append(Lecturers.query.filter_by(id=int(i)).first())
        students_accepted = []; lecturers_accepted = [];
        if lecturer.students_accepted != None:
            for i in lecturer.students_accepted.split(','):
                students_accepted.append(Students.query.filter_by(id=int(i)).first())
        if lecturer.lecturers_accepted != None:
            for i in lecturer.lecturers_accepted.split(','):
                lecturers_accepted.append(Lecturers.query.filter_by(id=int(i)).first())
        return render_template('dashboard/lecturer_requests.html',
                           the_title='Manage Requests - myTaraNG',
                           lecturerr=lecturer,
                           students_request=students_request,
                           lecturers_request=lecturers_request,
                           students_accepted=students_accepted,
                           lecturers_accepted=lecturers_accepted)

@app.route('/lecturer/lecturer_request_accept/<id>')
def lecturer_lecturer_request_accept(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer_requested = Lecturers.query.filter_by(id=id).first()
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        lecturers_request = list(set([int(i) for i in lecturer.lecturers_request.split(',')]))
        lecturers_request.remove(int(id))
        if lecturers_request:
            lecturers_request_str = ','.join(str(i) for i in lecturers_request)
            lecturer.lecturers_request = lecturers_request_str
            db.session.commit()
        else:
            lecturer.lecturers_request = None
            db.session.commit()

        if lecturer.lecturers_accepted:
            lecturer_accepted_list = list(set([int(i) for i in lecturer.lecturers_accepted.split(',')]))
            lecturer_accepted_list.append(lecturer_requested.id)
            lecturer_accepted_list_str = ','.join(str(i) for i in lecturer_accepted_list)
            lecturer.lecturers_accepted = lecturer_accepted_list_str
            db.session.commit()
        else:
            lecturer.lecturers_accepted = str(lecturer_requested.id)
            db.session.commit()

        if lecturer_requested.teachers:
            teachers_list = list(set([int(i) for i in lecturer_requested.teachers.split(',')]))
            teachers_list.append(lecturer.id)
            teachers_str = ','.join(str(i) for i in teachers_list)
            lecturer_requested.teachers = teachers_str
            db.session.commit()
        else:
            lecturer_requested.teachers = str(lecturer.id)
            db.session.commit()

        return redirect('/lecturer/requests')

@app.route('/lecturer/student_request_accept/<id>')
def lecturer_student_request_accept(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        student_requested = Students.query.filter_by(id=id).first()
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        students_request = list(set([int(i) for i in lecturer.students_request.split(',')]))
        students_request.remove(int(id))
        if students_request:
            students_request_str = ','.join(str(i) for i in students_request)
            lecturer.students_request = students_request_str
            db.session.commit()
        else:
            lecturer.students_request = None
            db.session.commit()

        if lecturer.students_accepted:
            student_accepted_list = list(set([int(i) for i in lecturer.students_accepted.split(',')]))
            student_accepted_list.append(student_requested.id)
            student_accepted_list_str = ','.join(str(i) for i in student_accepted_list)
            lecturer.students_accepted = student_accepted_list_str
            db.session.commit()
        else:
            lecturer.students_accepted = str(student_requested.id)
            db.session.commit()

        if student_requested.teachers:
            teachers_list = list(set([int(i) for i in student_requested.teachers.split(',')]))
            teachers_list.append(lecturer.id)
            teachers_str = ','.join(str(i) for i in teachers_list)
            student_requested.teachers = teachers_str
            db.session.commit()
        else:
            student_requested.teachers = str(lecturer.id)
            db.session.commit()

        return redirect('/lecturer/requests')



@app.route('/lecturer/lecturer_request_deny/<id>')
def lecturer_lecturer_request_deny(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        lecturers_request = list(set([int(i) for i in lecturer.lecturers_request.split(',')]))
        lecturers_request.remove(int(id))
        if lecturers_request:
            lecturers_request_str = ','.join(str(i) for i in lecturers_request)
            lecturer.lecturers_request = lecturers_request_str
            db.session.commit()
        else:
            lecturer.lecturers_request = None
            db.session.commit()
        return redirect('/lecturer/requests')


@app.route('/lecturer/student_request_deny/<id>')
def lecturer_student_request_deny(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        students_request = list(set([int(i) for i in lecturer.students_request.split(',')]))
        students_request.remove(int(id))
        if students_request:
            students_request_str = ','.join(str(i) for i in students_request)
            lecturer.students_request = students_request_str
            db.session.commit()
        else:
            lecturer.students_request = None
            db.session.commit()
        return redirect('/lecturer/requests')

@app.route('/lecturer/student_remove/<id>')
def lecturer_student_remove(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        student_removed = Students.query.filter_by(id=id).first()
        teachers_list = list(set([int(i) for i in student_removed.teachers.split(',')]))
        teachers_list.remove(session['lecturer_id'])
        if teachers_list:
            teachers_str = ','.join(str(i) for i in teachers_list)
            student_removed.teachers = teachers_str
            db.session.commit()
        else:
            student_removed.teachers = None
            db.session.commit()

        student_accepted_list = list(set([int(i) for i in lecturer.students_accepted.split(',')]))
        student_accepted_list.remove(id)
        if lecturer.students_accepted:
            student_accepted_list_str = ','.join(str(i) for i in student_accepted_list)
            lecturer.student_accepted = student_accepted_list_str
            db.session.commit()
        else:
            lecturer.students_accepted = None
            db.session.commit()
        return redirect('/lecturer/requests')


@app.route('/lecturer/student_remove/<id>')
def lecturer_lecturer_remove(id):
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        lecturer_removed = Lecturer.query.filter_by(id=id).first()
        teachers_list = list(set([int(i) for i in lecturer_removed.teachers.split(',')]))
        teachers_list.remove(session['lecturer_id'])
        if teachers_list:
            teachers_str = ','.join(str(i) for i in teachers_list)
            lecturer_removed.teachers = teachers_str
            db.session.commit()
        else:
            lecturer_removed.teachers = None
            db.session.commit()

        lecturer_accepted_list = list(set([int(i) for i in lecturer.lecturers_accepted.split(',')]))
        lecturer_accepted_list.remove(id)
        if lecturer.lecturers_accepted:
            lecturer_accepted_list_str = ','.join(str(i) for i in lecturer_accepted_list)
            lecturer.lecturers_accepted = lecturer_accepted_list_str
            db.session.commit()
        else:
            lecturer.lecturers_accepted = None
            db.session.commit()
        return redirect('/lecturer/studentsrequest')




########################################### Collaborate ####################################
@app.route('/lecturer/collaborate')
def lecturer_collaborate():
    if 'username' not in session:
        return redirect('/login')
    else:
        lecturer = Lecturers.query.filter_by(email=session['username']).first()
        return render_template('dashboard/collaborate.html',
                           the_title='Collaborate - myTaraNG',
                           lecturer=lecturer)


@app.route('/lecturer/collaborate_success', methods = ['POST', 'GET'])
def lecturer_collaborate_success():
    if 'username' not in session:
        return redirect('/login')
    elif request.method == 'POST':
        try:
            lecturer = Lecturers.query.filter_by(email=session['username']).first()
            assignment = Collaborates(lecturer.id,lecturer.id,topic_name,path1, topic_type, topic_abstract, topic_subject, topic_chapter)
            db.session.add(assignment)
            db.session.commit()
            flash('We received your request')
            return redirect('/lecturer/collaborate')
        except Exception:
            flash('Error occurred ! Please try again')
            return redirect('/lecturer/collaborate')
    else:
        flash('Error occurred ! Please try again')
        return redirect('/lecturer/collaborate')



if __name__ == '__main__':
    # app.run(debug = True,host = '0.0.0.0',port=5000)
    app.run(debug = True)







