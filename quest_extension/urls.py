from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    #path('', views.home, name='quest-home'),
    #path('quest-create-form', views.quest_create, name='quest_form'),
    #path('choose-mc-or-fr/<name>', views.choose_question_type),
    path('mc-create-form/<quest_id>', views.create_mc_question),
    path('fr-create-form/<quest_id>', views.create_fr_question),
    #path('more_questions/<name>', views.more_questions),
    #path('home', views.quest_home, name='home'),
    path('admin_home_editable/<project_id>', views.admin_home_editable),
    path('admin_quest_page_editable/<quest_id>', views.admin_quest_page_editable),
    path('user_home/<ldap>/<project_id>', views.user_home),
    path('user_quest_page/<ldap>/<quest_id>', views.user_quest_page),
    path('admin_edit_question/<question_id>', views.admin_edit_question),
    path('admin_project_page', views.admin_project_page),
    path('user_project_page/<ldap>', views.user_project_page),
    path('new_user', views.new_user),
    path('user_login', views.user_login),
    path('admin_home_view_only/<project_id>', views.admin_home_view_only),
    path('admin_quest_page_view_only/<quest_id>', views.admin_quest_page_view_only),






]
