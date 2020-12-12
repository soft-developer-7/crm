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



    //---------------------------------- Textarea Modal-------------------


var t_name="";

$("textarea").focusin(function(){
	t_name = this.id;
	var t_val = $('textarea[name='+t_name+']').val();
  $(".ql-editor").html(t_val);
  
  if(this.maxLength>0)
    limit = this.maxLength;
  else
    limit = 1000;
    
  $('#richtextModal').modal('toggle');
  quill.focus();
 
});


$('#get-content').click(function(){
	$('#richtextModal').modal("hide");
	var c = quill.getText();
	var h =  quill.root.innerHTML;
	$('#'+t_name).html(c);
	if(h!="<p><br></p>")
		$('textarea[name='+t_name+']').val(h);
	else
		$('textarea[name='+t_name+']').val('');

});


