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

# 註冊會員
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
# 登入會員
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
# 登出會員
@blog.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    flash("您已經登出")
    return redirect(url_for('index'))

# 發文
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
# 編輯文章
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
# 刪除文章
@blog.route('/articles/delete/<int:article_id>', methods=['POST'])
@login_required
def delete_article(article_id):
    from web.blog.model import Article
    article = Article.query.get_or_404(article_id)
    if article.user_id != current_user.id:
        abort(403)
    article.delete()
    return redirect(url_for('blog.articles'))
# 文章列表管理
@blog.route('/articles/edit_list_articles')
@blog.route('/articles/edit_list_articles/<int:page>/')
@login_required
def edit_list_articles(page=1):
    from web.blog.model import Article
    articles = Article.query.all()
    pages=Article.query.filter_by().paginate(page=page,per_page=15)
    return render_template('/blog/edit_list.html', articles=articles,pages=pages)
# 新增文章分類
@blog.route('/categories/add', methods=['POST'])
@login_required
def add_category():
    from web.blog.model import Category
    name = request.form.get('name')
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('blog.edit_list_category'))
# 編輯文章分類
@blog.route('/categories/edit/<int:category_id>', methods=['GET', 'POST'])
@login_required
def edit_category(category_id,page=1):
    from web.blog.model import Category
    from web.blog.form import CategoryForm
    category = Category.query.get_or_404(category_id)
    form = CategoryForm(obj=category)
    categorys = Category.query.all()
    pages=Category.query.filter_by().paginate(page=page,per_page=15)
    if form.validate_on_submit():
        form.populate_obj(category)
        db.session.commit()
        return redirect(url_for('blog.edit_list_category'))
    return render_template('blog/edit_list_category.html',categorys=categorys, form=form,pages=pages)
# 刪除文章分類
@blog.route('/articles/delete_category/<int:category_id>', methods=['GET', 'POST'])
@login_required
def delete_category(category_id):
    from web.blog.model import Category
    categorys = Category.query.get_or_404(category_id)
    categorys.delete()
    return redirect(url_for('blog.edit_list_category'))
# 文章分類管理
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
# 新增文章標籤
@blog.route('/tag/add', methods=['POST'])
@login_required
def add_tag():
    from web.blog.model import Tag
    name = request.form.get('name')
    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return redirect(url_for('blog.edit_list_tag'))
# 編輯文章標籤
@blog.route('/tag/edit/<int:tag_id>', methods=['GET', 'POST'])
@login_required
def edit_tag(tag_id,page=1):
    from web.blog.model import Tag
    from web.blog.form import TagForm
    tag = Tag.query.get_or_404(tag_id)
    form = TagForm(obj=tag)
    tags = Tag.query.all()
    pages=Tag.query.filter_by().paginate(page=page,per_page=15)
    if form.validate_on_submit():
        form.populate_obj(tag)
        db.session.commit()
        return redirect(url_for('blog.edit_list_tag'))
    return render_template('blog/edit_list_tag.html',tags=tags, form=form,pages=pages)
# 刪除文章標籤
@blog.route('/tag/delete_tag/<int:tag_id>', methods=['GET', 'POST'])
@login_required
def delete_tag(tag_id):
    from web.blog.model import Tag
    tags = Tag.query.get_or_404(tag_id)
    tags.delete()
    return redirect(url_for('blog.edit_list_tag'))
# 文章標籤管理
@blog.route('/tag/edit_list_tag')
@blog.route('/tag/edit_list_tag/<int:page>/')
@login_required
def edit_list_tag(page=1):
    from web.blog.model import Tag
    from web.blog.form import TagForm
    form = TagForm()
    tags = Tag.query.all()
    pages=Tag.query.filter_by().paginate(page=page,per_page=15)
    return render_template('/blog/edit_list_tag.html', tags=tags,pages=pages,form=form)
# 文章列表
@blog.route('/artcle_list/')
@blog.route('/artcle_list/<int:page>')
def artcle_list(page=1):
    from web.blog.model import Article
    artcle_list = Article.query.order_by(Article.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('/blog/list.html',artcle_list=artcle_list)
