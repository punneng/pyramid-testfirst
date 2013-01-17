var taskTemplate = "                <div id=\"todo_grid_${id}\" class=\"row-fluid show-grid priority_${priority}\"> \
                    <div class=\"span10\"> \
                        <label class=\"checkbox\"> \
                            <input type=\"checkbox\"> ${task} \
                        </label> \
                    </div> \
                    <div class=\"span2\"> \
                        <button id=\"edit-button\" type=\"submit\" class=\"btn edit\">Edit</button>
                    </div>
                </div>"
AppUtils = {
    formatStr : function(htmlTemplate, jsonVals){
        var template = htmlTemplate;
        for(var key in jsonVals){
            if (jsonVals.hasOwnProperty(key)) {
                template = template.replace("${"+key+"}", jsonVals[key])
            } 
        }

        return template;
    }
}
$(function() {

    $("#add-button").click(function() {
        $.post('/todos/create', $('#submit-form').serialize(), function(data) {
            if(data['errors']){
                // replace error str
                return;
            }
            //$('#todo-list').append(AppUtils.formatStr(taskTemplate, data));
            var newTodo = AppUtils.formatStr(taskTemplate, data);
            if($(".priority_"+data['priority']).length > 0){
                $($(".priority_"+data['priority'])[0]).before(newTodo);
                window.location.hash = 'todo_grid_'+data['id'];
                $($(".priority_"+data['priority'])[0]).effect("highlight", {}, 3000);
            }else{
                
            }
            
 
            $("#task-input").val("");
        }, 'json');
    });
    
    $(".btn-priority .btn").click(function() {
        $('#priorty-input').val($(this).attr('priority'));
    });
});