$( document ).ready( function() {
  var api = "https://api.github.com/repos/darkmattervale/regex4dummies/issues";
  $.get(api, function (data) {
    $.each(data, function (idx, obj) {
      var add_progress_table = false;
      var add_todo_table     = false;

      var progress = "Due: Continuous";

      for ( var index = 0; index < obj.labels.length; index++ ) {

        if ( JSON.stringify( "Objective" ) == JSON.stringify( obj.labels[index].name ) ) {
          add_todo_table = true;
        } else if ( JSON.stringify( "In-Progress" ) == JSON.stringify( obj.labels[index].name ) ) {
          add_progress_table = true
        }
      }
      try {
        if ( obj.milestone.due_on ) {
          progress = "Due: " + obj.milestone.due_on.substring(0, 10);
        }
      } catch( err ) {
      }

      if ( add_progress_table ) {
        $("#progress_table").append( " \
          <table class='pure-table pure-table-horizontal' width='100%' height='auto'> \
            <tr> \
              <td> \
                <h4><a href='" + obj.html_url + "'>" + obj.title + "</a></h4> \
              </td> \
              <td></td><td></td><td></td> \
            </tr> \
            <tr class='pure-table-odd'> \
              <td> \
                <img src='" + obj.user.avatar_url + "' width='28px' height='28px'>" + "     " + obj.user.login + "</img> \
              </td> \
              <td></td><td></td><td style='text-align: right;'>" + progress + "</td> \
            </tr> \
          </table>" );
      } else if ( add_todo_table ) {
        $("#todo_table").append( " \
          <table class='pure-table pure-table-horizontal' width='100%' height='auto'> \
            <tr> \
              <td> \
                <h4><a href='" + obj.html_url + "'>" + obj.title + "</a></h4> \
              </td> \
              <td></td><td></td><td></td> \
            </tr> \
            <tr class='pure-table-odd'> \
              <td> \
                <img src='" + obj.user.avatar_url + "' width='28px' height='28px'>" + "     " + obj.user.login + "</img> \
              </td> \
              <td></td><td></td><td style='text-align: right;'>" + progress + "</td> \
            </tr> \
          </table>" );
      }
    });
  });
});
