$( document ).ready( function() {
  var api = "https://api.github.com/repos/darkmattervale/regex4dummies/milestones";
  $.get(api, function (data) {
    var most_recent_milestone_month    = 12;
    var most_recent_milestone_day      = 31;
    var most_recent_milestone_name     = "";
    var most_recent_milestone_due_date = "";
    var most_recent_milestone_url      = "";
    var most_recent_milestone_complete = 0;

    $.each(data, function (idx, obj) {
      var test_milestone_month = Number( obj.due_on.substring(5, 7) );
      var test_milestone_day   = Number( obj.due_on.substring(8, 10) );

      if ( test_milestone_month < most_recent_milestone_month ) {
        most_recent_milestone_day   = test_milestone_day;
        most_recent_milestone_month = test_milestone_month;
      } else if ( test_milestone_month == most_recent_milestone_month ) {
        if ( test_milestone_day < most_recent_milestone_day ) {
          most_recent_milestone_day   = test_milestone_day;
          most_recent_milestone_month = test_milestone_month;
        }
      }

      most_recent_milestone_url      = obj.html_url;
      most_recent_milestone_name     = obj.title;
      most_recent_milestone_due_date = most_recent_milestone_month + "-" + most_recent_milestone_day + "-" + obj.due_on.substring(0, 4);
      most_recent_milestone_complete = Number( obj.closed_issues ) / ( Number( obj.open_issues ) + Number( obj.closed_issues ) ) * 100;
    });

    $("#milestone_table").append( " \
      <table class='pure-table pure-table-horizontal' width='100%' height='auto'> \
        <tr> \
          <td> \
            <h4><a href='" + most_recent_milestone_url + "'> v" + most_recent_milestone_name + "</a></h4> \
          </td> \
          <td></td><td></td><td style='text-align: right;'> \
          <style>progress[value]::-webkit-progress-value::before { \
            content: '" + most_recent_milestone_complete + "%'; \
            position: relative; \
            right: 0; \
            top: -125%; \
          }</style> \
          <progress value='" + most_recent_milestone_complete + "' max='100'></progress></td> \
        </tr> \
        <tr class='pure-table-odd'> \
          <td>Author: Vale Tolpegin</td><td></td><td></td><td style='text-align: right;'>" + "Arriving on " + most_recent_milestone_due_date + "</td> \
        </tr> \
      </table>" );
  });
});
