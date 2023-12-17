function test(){
    $('#btn').click(function(){
        $.ajax('/project_create/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#id_name').val()
            },
            'success': function(data){
                document.getElementById('tasks').innerHTMl += data
            }
        })
    })
}

$(function(){
    $('#btn').click(function(){
        var button = $(this)
        $.ajax(button.data('url'), {
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'name': $('#name').val(),
                'status': $('#status').val(),       // on off
                'deadline': $('#id_deadline').val(),
                'priority': $('#id_priority').val()
            },
            'success': function(data){
                document.getElementById('tasks').innerHTML += data
            }
        })
    })
})


$(function(){
    $(document).click(function(event){
        var element = $(event.target);
        if (element.attr('class') == 'edit_task') {
            $.ajax(element.data('url'), {
                'type': 'POST',
                'async': true,
                'dataType': 'json',
                'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id': element.attr('id')
                }
            })
        }
    })
})
$(document).ready(function(){
    test();
})

