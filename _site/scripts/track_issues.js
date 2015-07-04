$( document ).ready( function() {
  /*var github = new Github({});
  var issues = github.getIssues( "DarkmatterVale", "regex4dummies" );
  console.log( issues );

  for ( var issue in issues ) {
    $( '#in-progress-block' ).append( "<li>" + issue.)
  }*/

  $.ajax({
    url: "https://api.github.com/repos/darkmattervale/regex4dummies/issues",
    dataType: "json",
    success: function ( returnData ) {
      //$("#in-progress-block").html(returnData[0]["object"]["sha"]);
      alert('Load was performed.');
      alert( JSON.parse( returnData[0].object.sha ) );
    }
  });

  for ( var x = 0; x < 10; x++ ) {
    $( '#in-progress-block' ).append( "<li>YOLO</li>" );
  }
});
