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

$(document).ready(function() {
  $(".delete").hide();
  //when the Add Field button is clicked
  $("#add-listing-button").click(function(e) {
    //Append a new row of code to the "#items" div
     var input_fields = $(".add-listing")
    $("#add-listing-container").append(
                        '<div class="row clearfix add-listing"> \
                                    <div class="col-lg-12">\
                                    <p>\
                                    <b>Book/listing</b>&nbsp;<a class="delete-listing"><small>delete</small></a>\
                                    </p>\
                                    </div>\
                                  <div class="col-lg-6">\
                                    <div class="form-group form-float">\
                                        <div class="form-line">\
                                            <input type="text" class="form-control inputBold" name="title" required>\
                                            <label class="form-label"><b>Title*</b></label>\
                                        </div>\
                                  </div>\
                                    </div>\
                                    <div class="col-lg-2">\
                                        <select class="form-control show-tick" name="year" value="year">\
                                            <option value="" disabled selected>Type</option>\
                                            <option value="B">Book</option>\
                                            <option value="R">Reading</option>\
                                        </select>\
                                    </div>\
                                    <div class="col-lg-4">\
                                      <div class="form-group form-float">\
                                          <div class="form-line">\
                                              <input type="text" class="form-control inputBold" name="title" required>\
                                              <label class="form-label"><b>Edition (Leave blank for reading)</b></label>\
                                          </div>\
                                    </div>\
                                      </div>\
                                      <div class="col-lg-3">\
                                        <div class="form-group form-float">\
                                            <div class="form-line">\
                                                <input type="text" class="form-control inputBold" name="title" required>\
                                                <label class="form-label"><b>Condition</b></label>\
                                            </div>\
                                      </div>\
                                        </div>\
                                      <div class="col-lg-5">\
                                        <div class="form-group form-float">\
                                            <div class="form-line">\
                                                <input type="text" class="form-control inputBold" name="title" required>\
                                                <label class="form-label"><b>Additional Info (optional)</b></label>\
                                            </div>\
                                      </div>\
                                      </div>\
                                      <div class="form-group">\
                                          <input type="file" id="file" name="file">\
                                          <small><label for="file">* Upload a clear image of book/reading</label></small>\
                                      </div>\
                                  </div>'
    );
  });
  $("body").on("click", ".delete", function(e) {
    $(".next-referral").last().remove();
  });
});
