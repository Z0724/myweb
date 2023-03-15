from . import blog
from web.blog.form import RegForm, LoginForm
from web.model import User
from web.expand.other import mail, db
from flask import abort, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask_login import current_user

# 會員資料頁面
@blog.route('/<int:user_id>')
@login_required
def user_home(user_id):
    user =  User.query.find_one_or_404({'_id': user_id})
    return render_template('blog/user_home.html', user=user)


# 顯示文章內容
@blog.route('/article/<int:article_id>')
def article(article_id):
    from .model import Article
    article = Article.query.get(article_id)
    if not article:
        abort(404)
    return render_template('/blog/article.html', article=article)


@blog.route('/reg',methods=['POST','GET'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data, password=form.password.data)
        # add to db table
        db.session.add(user)
        db.session.commit()
        flash("註冊成功")
        return redirect(url_for('blog.login'))
    return render_template('/users/reg.html', form=form)

@blog.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            # 第二個參數是記得我的參數
            login_user(user, form.remember_me.data)
            flash("您已經成功的登入系統")
            # 利用request來取得參數next，上個頁面在哪
            next = request.args.get('next')
            # 自定義一個驗證的function來確認使用者是否確實有該url的權限
            # 另一個用法if not next_is_valid(next):
            # next_is_valid需要另外寫函式next_is_valid(url):return True
            if  next == None or not next[0]=='/':
                next = url_for('index')
            return redirect(next)
        else:
            #  如果資料庫無此帳號或密碼錯誤，就顯示錯誤訊息。
            flash('信箱或密碼錯誤')
    return render_template('/users/login.html',form=form)

@blog.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    flash("您已經登出")
    return redirect(url_for('index'))


@blog.route('/Article/post',methods=['POST','GET'])
def Articless():
    from web.blog.form import ArticleForm
    form = ArticleForm()
    if form.validate_on_submit():
        from web.blog.model import Article,Tag
        Articles = Article(title=form.title.data,
                              content=form.content.data,
                              user_id=current_user.id,
                              category_id=form.category_id.data
                              )
        Articles.tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()
        # add to db table
        db.session.add(Articles)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('/blog/post.html', form=form)

@blog.route('/Article/edit/<int:article_id>', methods=['GET', 'POST'])
@login_required
def edit_article(article_id):
    from web.blog.form import ArticleForm
    from web.blog.model import Article,Tag
    article = Article.query.get_or_404(article_id)
    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        form.populate_obj(article)
        article.tags = Tag.query.filter(Tag.id.in_(form.tags.data)).all()
        db.session.commit()
        return redirect(url_for('blog.article', article_id=article.id))
    return render_template('/blog/edit.html', form=form)

@blog.route('/articles/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    from web.blog.model import Article
    article = Article.query.get_or_404(article_id)
    if article.user_id != current_user.id:
        abort(403)
    article.delete()
    return redirect(url_for('blog.articles'))

@blog.route('/articles/edit_list_articles')
@blog.route('/articles/edit_list_articles/<int:page>/')
@login_required
def edit_list_articles(page=1):
    from web.blog.model import Article
    articles = Article.query.all()
    pages=Article.query.filter_by().paginate(page=page,per_page=15)
    return render_template('/blog/edit_list.html', articles=articles,pages=pages)

@blog.route('/categories/add', methods=['POST'])
@login_required
def add_category():
    from web.blog.model import Category
    name = request.form.get('name')
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('blog.edit_list_category'))

@blog.route('/categories/edit/<int:category_id>', methods=['GET', 'POST'])
@login_required
def edit_category(category_id,page=1):
    from web.blog.model import Category
    from web.blog.form import CategoryForm
    categorys_id = Category.query.get_or_404(category_id)
    categorys = Category.query.all()
    form = CategoryForm(obj=categorys_id)
    pages=Category.query.filter_by().paginate(page=page,per_page=15)
    if form.validate_on_submit():
        form.populate_obj(categorys_id)
        db.session.commit()
        return redirect(url_for('blog.edit_list_category'))
    return render_template('blog/edit_list_category.html',categorys=categorys,pages=pages, form=form)

@blog.route('/articles/delete_category/<int:category_id>', methods=['GET', 'POST'])
@login_required
def delete_category(category_id):
    from web.blog.model import Category
    categorys = Category.query.get_or_404(category_id)
    categorys.delete()
    return redirect(url_for('blog.edit_list_category'))


@blog.route('/articles/edit_list_category')
@blog.route('/articles/edit_list_category/<int:page>/')
@login_required
def edit_list_category(page=1):
    from web.blog.model import Category
    from web.blog.form import CategoryForm
    form = CategoryForm()
    categorys = Category.query.all()
    pages=Category.query.filter_by().paginate(page=page,per_page=15)
    return render_template('/blog/edit_list_category.html', categorys=categorys,pages=pages,form=form)


# @blog.route('/categories/edit/<int:category_id>', methods=['GET', 'POST'])
# @login_required
# def edit_category(category_id, page=1):
#     from web.blog.model import Category
#     from web.blog.form import CategoryForm
#     category = Category.query.get_or_404(category_id)
#     form = CategoryForm(obj=category)
#     form.operation.data = "edit"  # 添加一个隐藏字段，表示当前操作为编辑分类
#     if form.validate_on_submit():
#         if form.operation.data == "edit":  # 编辑分类
#             form.populate_obj(category)
#         else:  # 新增分类
#             new_category = Category()
#             form.populate_obj(new_category)
#             db.session.add(new_category)
#         db.session.commit()
#         return redirect(url_for('blog.edit_list_category'))
#     return render_template('blog/edit_category.html', form=form)