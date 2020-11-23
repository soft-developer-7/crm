var toolbarOptions = [
  ['bold', 'italic', 'underline'],
  [{ 'list': 'ordered'}, { 'list': 'bullet' }],
  [{ 'header': [1, 2, 3,false] }],
];

var quill = null;

$(document).ready(function(){
    quill = new Quill('#editor', {
      modules: {
        toolbar: toolbarOptions
      },




      



      theme: 'snow'
    });
    

});

