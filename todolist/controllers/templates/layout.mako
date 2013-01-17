<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Todolist</title>
    
    <!-- bootstrap -->
    <link rel="stylesheet" href="${request.static_url('todolist:static/bootstrap/css/bootstrap.min.css')}" type="text/css" media="screen" charset="utf-8" />
    <!-- /bootstrap -->
    <link rel="stylesheet" href="${request.static_url('todolist:static/css/jquery-ui-1.9.1.custom.min.css')}" type="text/css" media="screen" charset="utf-8" />
    <link rel="stylesheet" href="${request.static_url('todolist:static/css/styles.css')}" type="text/css" media="screen" charset="utf-8" />
    
    <script src="${request.static_url('todolist:static/js/jquery-1.8.2.min.js')}"></script>
    <script src="${request.static_url('todolist:static/js/jquery-ui-1.9.1.custom.min.js')}"></script>
    <script src="${request.static_url('todolist:static/bootstrap/js/bootstrap.min.js')}"></script>
    <script src="${request.static_url('todolist:static/js/app.js')}"></script>

</head>
<body>
    <div id="container">
        <div id="header">
            Todolist
        </div>
        <div id="content">
            ${self.content()}
        </div>
    </div>
</body>
</html>