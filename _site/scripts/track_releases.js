$( document ).ready( function() {
  var assembled_versions = [];
  var assembled_releases = [ [] ];
  var api = "https://api.github.com/repos/darkmattervale/regex4dummies/releases";

  $.get(api, function (data) {
    $.each(data, function (idx, obj) {
      var major_version = JSON.stringify( obj.tag_name ).split( '.' )[0];
      var major_version_length = major_version.length;
      major_version = major_version.substring( major_version_length - 1, major_version_length )

      var sub_version = JSON.stringify( obj.tag_name ).split( '.' )[1];
      var sub_version_length = sub_version.length;
      sub_version = sub_version.substring( sub_version_length - 1, sub_version_length )

      var minor_version = JSON.stringify( obj.tag_name ).split( '.' )[2];
      var minor_version_length = minor_version.length;
      minor_version = minor_version.substring( minor_version_length - 1, minor_version_length )

      var head_version = major_version + "." + sub_version;

      try {
        var add = true;
        for ( var index = 0; index < assembled_versions.length; index++ ) {
          if ( assembled_versions[ index ] == head_version ) {
            add = false;

            break;
          }
        }

        if ( add ) {
          assembled_versions.push( head_version );

          document.getElementById( "menu" ).innerHTML += "<li class='pure-menu-item'><a href='#menu_" + major_version + "." + sub_version + "' class='pure-menu-link'>" + head_version + "</a></li>";
        }
      } catch ( err ) {
        assembled_versions.push( head_version );
      }

      assembled_releases.push( [ head_version, obj.name, obj.body, obj.zipball_url, obj.tarball_url ] );
    });

    for ( var version_index = 0; version_index < assembled_versions.length; version_index++ )
    {
      var code = "<h2>" + assembled_versions[version_index] + "</h2><div id='menu_" + assembled_versions[version_index] + "'>";

      for ( var release_index = 0; release_index < assembled_releases.length; release_index++ )
      {
        if ( assembled_releases[release_index][0] == assembled_versions[version_index] )
        {
          code += "<table class='pure-table pure-table-horizontal' width='100%' height='auto'><tr> \
            <td> \
              <h4>" + assembled_releases[release_index][1] + "</h4> \
            </td> \
            <td> \
              <a class='text-right' href='" + assembled_releases[ release_index ][ 3 ] + "'>zip download</a> \
            </td> \
            <td> \
              <a class='text-right' href='" + assembled_releases[ release_index ][ 4 ] + "'>tar download</a> \
            </td> \
          </tr> \
          <tr class='pure-table-odd'> \
            <td><p>" + assembled_releases[ release_index ][ 2 ] + "</p></td> \
            <td></td><td></td> \
          </tr></table>";
        }
      }

      code += "</div>";

      $("#version_container").append( code );
    }
  });
});
