<%inherit file="/layout.mako"/>

<%def name="content()">

<div class="tabbable" id="main-tabs"> <!-- Only required for left/right tabs -->
    <ul class="nav nav-tabs">
        <li class="active"><a href="#tab1" data-toggle="tab">Todo</a></li>
        <li><a href="#tab2" data-toggle="tab">Done</a></li>
        <li><a href="#tab3" data-toggle="tab">Info</a></li>
    </ul>
    <div class="tab-content">
        <div class="tab-pane active" id="tab1">
            <div id="todo-form">
                <form id="submit-form" onsubmit="return false;">
                    <div class="row-fluid show-grid element-line">
                        <div class="span10">
                            <input type="text" class="input-fit-large text-field" placeholder="Task" name="task" id="task-input">
                            <input type="hidden" name="priority" id="priorty-input" value="5">
                        </div>
                        <div class="span2"><button id="add-button" type="submit" class="btn add">Add</button></div>
                    </div>
                    <div class="btn-group btn-priority" data-toggle="buttons-radio">
                        <button type="button" class="btn btn-primary" priority="0">Easy</button>
                        <button type="button" class="btn active" priority="5">Ok</button>
                        <button type="button" class="btn btn-danger" priority="10">Urgent</button>
                    </div>
                </form>
            </div>
            <div class="todo-list" id="todo-list">
                <div class="priority_10"></div>
                <div class="priority_5"></div>
                <div class="priority_0"></div>
                % for todo in todos:
                <div id="todo_grid_${todo.id}" class="row-fluid show-grid priority_${todo.priority}">
                    <div class="span10">
                        <label class="checkbox">
                            <input type="checkbox"> ${todo.task}
                        </label>
                    </div>
                    <div class="span2">
                        <button id="edit-button" type="submit" class="btn edit">Edit</button>
                    </div>
                </div>
                % endfor
                <!--
                <div class="row-fluid show-grid">
                    <div class="span12">
                        <label class="checkbox">
                            <input type="checkbox"> Check me out
                        </label>
                    </div>
                </div>
                <div class="row-fluid show-grid">
                    <div class="span12">
                        <label class="checkbox">
                            <input type="checkbox"> Check me out
                        </label>
                    </div>
                </div>
                <div class="row-fluid show-grid">
                    <div class="span12">
                        <label class="checkbox">
                            <input type="checkbox"> Check me out
                        </label>
                    </div>
                </div>
                <div class="row-fluid show-grid last">
                    <div class="span12">
                        <label class="checkbox">
                            <input type="checkbox"> Check me out
                        </label>
                    </div>
                </div>
                -->
            </div>
        </div>
        <div class="tab-pane" id="tab2">
            <div class="todo-list">
                <div class="row-fluid show-grid">
                    <div class="span12">
                        Check me out
                    </div>
                </div>
                <div class="row-fluid show-grid">
                    <div class="span12">
                        Check me out
                    </div>
                </div>
                <div class="row-fluid show-grid">
                    <div class="span12">
                        Check me out
                    </div>
                </div>
                <div class="row-fluid show-grid">
                    <div class="span12">
                        Check me out
                    </div>
                </div>
            </div>
        </div>
        <div class="tab-pane" id="tab3">
            <p>Howdy, I'm in Section 3.</p>
        </div>
    </div>
</div>




</%def>