var limit=1000; // default character limit

var toolbarOptions = [
    ['bold', 'italic', 'underline'],
    [{ 'list': 'ordered'}, { 'list': 'bullet' }],
    [{ 'header': [1, 2, 3, 4,false] }],
    /*['clean']*/                                         
  ];

 

  
  Quill.register('modules/counter', function(quill, options) {

    var container = document.querySelector(options.container);
    quill.on('text-change', function() {
      var text = quill.getText();

      if (options.unit === 'word') 
      {
        container.innerText = text.split(/\s+/).length + ' words';
      } 

      else 
      {
        var c_l = (text.length-1);
        

        if(c_l>limit)
        {
           limit_exceed();
           container.innerText = (limit-c_l) + ' Characters';
        }

        else
        {
          under_limit()
          container.innerText = c_l + ' Characters';
        }
          
        
      }
      
    });


  });


  var quill = new Quill('#editor-container', { 
    modules: { 
      toolbar: toolbarOptions,
      counter: {
        container: '#counter',
        unit: 'character'
      } /*,keyboard: {
        bindings: {
          'tab': {
            key: 9,
            handler: function(range, context) {
              return true;
            }
          }
        }
      } */
    },

    
    placeholder: 'Write here...',
    theme: 'snow' });
  





    function limit_exceed()
    {
      $("#err").html('<p class="text-danger">('+limit+' Characters) Limit Exceed !</p>');
      $("#get-content").prop('disabled', true);
    }

    function under_limit()
    {
      $("#err").html('');
      $("#get-content").prop('disabled', false);
    }



    //---------------------------------- Div touch to Modal-------------------


var cur_box="";

$("body").on("click",".inputbox", function(){
  cur_box=this.id;
  var t_val = $(this).find('input').val();
  var maxlen = $('#'+cur_box+' input').attr('maxLength');
  $(".ql-editor").html(t_val);
  
  if(maxlen>0)
    limit = maxlen;
  else
    limit = 1000;
    
  $('#richtextModal').modal('toggle');
  quill.focus();
 
});


$('#get-content').click(function(){
	$('#richtextModal').modal("hide");
	//var c = quill.getText();         //Plain text
	var h =  quill.root.innerHTML;
	$('#'+cur_box+' .content').html(h);
	if(h!="<p><br></p>")
		$("#"+cur_box+' input').val(h);
	else
  $("#"+cur_box+' input').val("");

});


