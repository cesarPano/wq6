requirejs.config({
    'baseUrl': '/js/lib',
    'paths': {
        'wqproject': '../wqproject',
        'data': '../data/'
    }
});

requirejs(['wqproject/main']);
