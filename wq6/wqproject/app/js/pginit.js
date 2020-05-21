function getBaseUrl() {
    var baseurl = window.location.pathname.replace("index.html",'');
    baseurl = baseurl.replace(/\/$/,'');
    if (baseurl == 'www') {
        // Windows
        baseurl = '/www';
    }
    return baseurl;
}

require.config({
    'config': {
        'wqproject/config': {
             'router': {
                 'base_url': getBaseUrl()
             },
             'store': {
                 'service': 'https://wqproject.example.org',
                 'defaults': {'format': 'json'}
             },
        }
    }
});

document.addEventListener('deviceready', function() {
    require(['js/wqproject'], function() {
        require(['wqproject/main', 'wq/app'], function(ready, app) {
            ready.then(function() {
                app.replaceState('');
                setTimeout(navigator.splashscreen.hide, 10);
            });
        });
    });
});
