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
    var action_url = $(this).attr('url');
    var btn_div = $(this).parent()[0];
    var info_div = $(this).parent('div').next('.seller-info-box')[0];

    // Confirm box
    if (confirm("Confirm to get seller details.")) {
         $.ajax({
           url: "http://127.0.0.1:8000/add_interested" + '?type=' + type + '&id=' + entityid,
           type: 'GET',
           success: function(response){
                     // Removing row from HTML Table
                     if (response.message == 'Success'){
                       // alert("Success");
                       btn_div.remove();
                       info_div.style.display = "block";
                       info_div.querySelector("#seller_name").innerHTML = response.seller_name;
                       info_div.querySelector("#seller_email").innerHTML = response.seller_email;
                       info_div.querySelector("#seller_college").innerHTML = response.seller_college;
                     }else{
                       alert("Invalid Request, Please try again later.");
                     }
                    }
    });
  }
});
});
$(document).ready(function() {

  $('.item-picture').click(function(){
    var img_id = $(this).attr('id');
    var img_src = $(this).attr('src');

    var modal = document.querySelector('.item-img-modal');
    modal.style.display = "block";
    var modal_img = modal.querySelector('.modal-content');
    modal_img.src = img_src;
    var close_button = modal.querySelector(".close-modal");
    close_button.onclick = function() {
    modal.style.display = "none";
    }
});
});
