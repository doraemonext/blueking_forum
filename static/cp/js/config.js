require.config({
    baseUrl: '/static/cp/js',
    shim: {
        'underscore': { 'exports': '_' },
        'backbone-paginator': { 'deps': ['backbone'] },
        'bootstrap': { 'deps': ['jquery'] },
        'jquery-cookie': { 'deps': ['jquery'] },
        'noty': { 'deps': ['jquery'] },
        'jquery-validate': { 'deps': ['jquery'] },
        'jquery-form': { 'deps': ['jquery'] },
        'spin': { 'exports': 'Spinner' },
        'ckeditor': { 'exports': 'CKEDITOR' },
        'theme-app': { 'deps': ['jquery', 'bootstrap'] }
    },
    paths: {
        'jquery': 'plugins/jquery/jquery.min',

        'underscore': 'plugins/underscore/underscore.min',
        'backbone': 'plugins/backbone/backbone.min',

        'backbone-paginator': 'plugins/backbone/backbone.paginator.min',
        'bootstrap': 'plugins/bootstrap/bootstrap.min',
        'jquery-ui': 'plugins/jquery-ui/jquery-ui.min',
        'jquery-cookie': 'plugins/jquerycookie/jquery.cookie',
        'jquery-validate': 'plugins/jqueryvalidate/jquery.validate.min',
        'jquery-form': 'plugins/jqueryform/jquery.form',
        'noty': 'plugins/noty/jquery.noty.packaged.min',
        'spin': 'plugins/spin/spin.min',
        'ckeditor': 'plugins/ckeditor/ckeditor',
        'theme-app': 'plugins/inspinia/inspinia',
        'common': 'common'
/*
        'module.common.app-view': 'module/common/app_view',
        'module.common.app-breadcrumb-view': 'module/common/app_breadcrumb_view',
        'module.common.app-content-header-view': 'module/common/app_content_header_view',
        'module.official-account': 'module/official_account',
        'module.library.music': 'module/library/music',
        'module.library.news': 'module/library/news',

        'helper.confirm-modal': 'helper/confirm_modal/confirm_modal'
*/
    }
});