$.fn.child = function(s) {
    return $(this).children(s)[0];
}
$( document ).ready(function() {
  
    var parent_file_upload = document.getElementsByClassName('file-upload')
    var file_upload_input  = document.querySelectorAll('.file-upload input[type=file]')
    $('.file-upload').html('')
    for (let index = 0; index < parent_file_upload.length; index++) {
        parent_file_upload[index].appendChild ( file_upload_input[index])
    }

    var parent_file_upload = document.getElementsByClassName('url')
    var file_upload_input  = document.querySelectorAll('.vURLField')
    $('.url').html('')
    for (let index = 0; index < parent_file_upload.length; index++) {
        parent_file_upload[index].appendChild ( file_upload_input[index])
    }

    // $('#img-delete').click(function (e) {
    //     e.preventDefault()
    //     var file = $(this).next()
    //     var file = $(this).next().find('input[type="file"]').get(0)
    //     console.log(file)
    //     $(this).prevAll().remove();
    //     $(this).remove()


    // })

});  
