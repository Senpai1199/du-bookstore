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

