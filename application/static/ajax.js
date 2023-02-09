$(function(){

    $(document).on( 'click', '#register', function(event){
        event.preventDefault();

        // var id_client = $('#id_client').val();
        var id = $('#id').val();
        var nom_client = $('#nom_client').val();
        var prenom_client = $('#prenom_client').val();
        var email_client = $('#email_client').val();
        var entreprise_client = $('#entreprise_client').val();
        var password_client = $('#password_client').val();
        var _token = $('input[type="hidden"]').attr('value');

        $.ajax({

            url : "Ajax_lient_store",
            data : {
                id,
                nom_client,
                prenom_client,
                email_client,
                entreprise_client,
                password_client,
                _token 
            },
            dataType : 'json',
            method : "POST",
             success: function(data){
                 $("#formulaire :input").html('');
                //  $("#resultmatable").show();
                //  for ( let index= à ; index< data.length; index++){
                //      $('#matable').append(
                //          '<tr><td>'+ data[index].nom_client + '</td></tr>'
                        
                        
                        
                //      );

                //  }
             }

        });

    })

    $(document).on( 'click', '#edit', function(event){
        

        // var id_client = $('#id_client').val();
        var id = $('#id').val();
        var nom_client = $('#nom_client').val();
        var prenom_client = $('#prenom_client').val();
        var email_client = $('#email_client').val();
        var entreprise_client = $('#entreprise_client').val();
        var password_client = $('#password_client').val();
        var _token = $('input[type="hidden"]').attr('value');

        $.ajax({

            url : ("Ajax_edit/"+String(id)).replace(/ /g,''),
            data : {
                id,
                nom_client,
                prenom_client,
                email_client,
                entreprise_client,
                password_client,
                _token 
            },
            dataType : 'json',
            method : "GET",
             success: function(data){
                 $("#formulaire :input").html('');
                //  $("#resultmatable").show();
                //  for ( let index= à ; index< data.length; index++){
                //      $('#matable').append(
                //          '<tr><td>'+ data[index].nom_client + '</td></tr>'
                        
                        
                        
                //      );

                //  }
             }

        });

    })
    
    
    });