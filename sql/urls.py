# -*- coding: UTF-8 -*- 

from django.urls import path, re_path
from sql import views, views_ajax, query, slowlog, instance, db_diagnostic, charts, sql_tuning, groupmgmt
from sql.utils import jobs

urlpatterns = [
    re_path(r'^$', views.sqlworkflow),
    path('index/', views.sqlworkflow),
    path('login/', views.login, name='login'),
    path('logout/', views.sign_out),
    path('signup/', views.sign_up),
    path('sqlworkflow/', views.sqlworkflow),
    path('submitsql/', views.submitSql),
    path('editsql/', views.submitSql),
    path('submitotherinstance/', views.submitSql),
    path('detail/<int:workflowId>/', views.detail, name='detail'),
    path('autoreview/', views.autoreview),
    path('passed/', views.passed),
    path('execute/', views.execute),
    path('timingtask/', views.timingtask),
    path('cancel/', views.cancel),
    path('rollback/', views.rollback),
    path('sqlquery/', views.sqlquery),
    path('slowquery/', views.slowquery),
    path('sqladvisor/', views.sqladvisor),
    path('slowquery_advisor/', views.sqladvisor),
    path('queryapplylist/', views.queryapplylist),
    path('queryapplydetail/<int:apply_id>/', views.queryapplydetail, name='queryapplydetail'),
    path('queryuserprivileges/', views.queryuserprivileges),
    path('dbdiagnostic/', views.dbdiagnostic),
    path('workflow/', views.workflows),
    path('workflow/<int:audit_id>/', views.workflowsdetail),
    path('dbaprinciples/', views.dbaprinciples),
    path('charts/', charts.pyecharts),
    path('group/', views.group),
    path('grouprelations/<str:group_name>/', views.groupmgmt),
    path('instance/', views.instance),
    path('instanceuser/<str:instance_name>/', views.instanceuser),
    path('config/', views.config),

    path('authenticate/', views_ajax.authenticateEntry),
    path('sqlworkflowlist/', views_ajax.sqlworkflowlist),
    path('simplecheck/', views_ajax.simplecheck),
    path('getOscPercent/', views_ajax.getOscPercent),
    path('getWorkflowStatus/', views_ajax.getWorkflowStatus),
    path('stopOscProgress/', views_ajax.stopOscProgress),
    path('del_sqlcronjob/', jobs.del_sqlcronjob),

    path('workflow/list/', views_ajax.workflowlist),
    path('config/change/', views_ajax.changeconfig),

    path('group/group/', groupmgmt.group),
    path('group/addrelation/', groupmgmt.addrelation),
    path('group/relations/', groupmgmt.associated_objects),
    path('group/instances/', groupmgmt.instances),
    path('group/unassociated/', groupmgmt.unassociated_objects),
    path('group/auditors/', groupmgmt.auditors),
    path('group/changeauditors/', groupmgmt.changeauditors),

    path('instance/list/', instance.lists),
    path('instance/users/', instance.users),
    path('instance/getdbNameList/', instance.getdbNameList),
    path('instance/getTableNameList/', instance.getTableNameList),
    path('instance/getColumnNameList/', instance.getColumnNameList),

    path('query/', query.query),
    path('query/querylog/', query.querylog),
    path('query/explain/', query.explain),
    path('query/applylist/', query.getqueryapplylist),
    path('query/userprivileges/', query.getuserprivileges),
    path('query/applyforprivileges/', query.applyforprivileges),
    path('query/modifyprivileges/', query.modifyqueryprivileges),
    path('query/privaudit/', query.queryprivaudit),

    path('slowquery/review/', slowlog.slowquery_review),
    path('slowquery/review_history/', slowlog.slowquery_review_history),
    path('slowquery/sqladvisor/', views_ajax.sqladvisorcheck),
    path('slowquery/sqltuning/', sql_tuning.tuning),

    path('db_diagnostic/process/', db_diagnostic.process),
    path('db_diagnostic/create_kill_session/', db_diagnostic.create_kill_session),
    path('db_diagnostic/kill_session/', db_diagnostic.kill_session),
    path('db_diagnostic/tablesapce/', db_diagnostic.tablesapce),
    path('db_diagnostic/trxandlocks/', db_diagnostic.trxandlocks),
]
