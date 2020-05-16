$(document).ready(function(){
    $('.chk input').on('change',function(){
        var value = $(this).parent('td').next('td').html();
        value = parseInt(value);
        if(this.checked == true) {
            $("#amount").html( parseInt($("#amount").html()) + value );
        }
        else {
            $("#amount").html( parseInt($("#amount").html()) - value );
        }
    });

    $('#selectAll').click(function(e){
        var table= $(e.target).closest('table');
        $('td input:checkbox',table).prop('checked',this.checked);
    });

    $('#selectAll1').click(function(e){
        var table= $(e.target).closest('table');
        $('td input:checkbox',table).prop('checked',this.checked);
    });
});

$(document).ready(function() {

  $('.confirm_interest').click(function(){
    // bookid
    var entityid = $(this).attr('id');
    var type = $(this).attr('type');
    var action_url = $(this).attr('url')
    // Confirm box
    if (confirm("Confirm to get seller details.")) {
         $.ajax({
           url: "http://127.0.0.1:8000/add_interested" + '?type=' + type + '&id=' + entityid,
           type: 'GET',
           success: function(response){
                     // Removing row from HTML Table
                     if (response == 'Success'){
                       console.log(response);
                     }else{
                       console.log(response);
                     }
                    }
    });
  }
});
});
