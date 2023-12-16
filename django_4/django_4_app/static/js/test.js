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

$(document).ready(function(){
    test();
})

$(function(){
    $('#btn').click(function(){

    })
})